"""Local practice server: serves the editor UI, runs tests, and records keystroke logs.

Usage:  python3 practice-env/server.py      then open http://localhost:8000
Logs are written to practice-env/logs/ (git-ignored).
"""
import json, os, subprocess, sys, tempfile, time
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

HERE = os.path.dirname(os.path.abspath(__file__))
PROBLEMS = os.path.join(HERE, "problems")
LOGS = os.path.join(HERE, "logs")
RUNNER = os.path.join(HERE, "runner.py")
SESSION_LOG = os.path.join(LOGS, f"session-{time.strftime('%Y%m%d-%H%M%S')}.jsonl")


def list_problems():
    out = []
    for slug in sorted(os.listdir(PROBLEMS)):
        pdir = os.path.join(PROBLEMS, slug)
        if not os.path.isdir(pdir):
            continue
        with open(os.path.join(pdir, "meta.json")) as f:
            meta = json.load(f)
        with open(os.path.join(pdir, "statement.md")) as f:
            statement = f.read()
        with open(os.path.join(pdir, "starter.py")) as f:
            starter = f.read()
        out.append({"slug": slug, "title": meta["title"], "difficulty": meta.get("difficulty", ""),
                    "statement": statement, "starter": starter, "method": meta["method"]})
    return out


def run_tests(slug, code):
    pdir = os.path.join(PROBLEMS, os.path.basename(slug))
    with open(os.path.join(pdir, "meta.json")) as f:
        method = json.load(f)["method"]
    tmp = tempfile.mkdtemp(prefix="practice-")
    code_path = os.path.join(tmp, "solution.py")
    with open(code_path, "w") as f:
        f.write(code)
    try:
        proc = subprocess.run(
            [sys.executable, RUNNER, code_path, os.path.join(pdir, "tests.json"), method],
            capture_output=True, text=True, timeout=10)
    except subprocess.TimeoutExpired:
        return {"compile_error": "Timed out after 10s (possible infinite loop)", "results": []}
    if proc.returncode != 0 or not proc.stdout.strip():
        return {"compile_error": proc.stderr.strip()[-2000:] or "Runner failed", "results": []}
    return json.loads(proc.stdout)


def append_events(events):
    os.makedirs(LOGS, exist_ok=True)
    with open(SESSION_LOG, "a") as f:
        for e in events:
            f.write(json.dumps(e) + "\n")


class Handler(BaseHTTPRequestHandler):
    def _send(self, status, body, ctype="application/json"):
        data = body.encode() if isinstance(body, str) else body
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            with open(os.path.join(HERE, "index.html"), "rb") as f:
                self._send(200, f.read(), "text/html; charset=utf-8")
        elif self.path == "/api/problems":
            self._send(200, json.dumps(list_problems()))
        else:
            self._send(404, json.dumps({"error": "not found"}))

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        try:
            body = json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            return self._send(400, json.dumps({"error": "bad json"}))
        if self.path == "/api/run":
            result = run_tests(body["slug"], body["code"])
            return self._send(200, json.dumps(result))
        if self.path == "/api/log":
            append_events(body.get("events", []))
            return self._send(200, json.dumps({"ok": True}))
        self._send(404, json.dumps({"error": "not found"}))

    def log_message(self, fmt, *args):
        pass  # keep the terminal quiet


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    print(f"Practice environment at http://localhost:{port}")
    print(f"Keystroke log: {SESSION_LOG}")
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
