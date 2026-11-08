"""Runs a user's Solution against tests.json in a subprocess. Prints JSON results."""
import json, sys
from typing import List

def main():
    code_path, tests_path, method = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(code_path) as f:
        source = f.read()
    with open(tests_path) as f:
        tests = json.load(f)
    results = []
    try:
        namespace = {"List": List}
        exec(compile(source, "solution.py", "exec"), namespace)
        solution = namespace["Solution"]()
        fn = getattr(solution, method)
    except Exception as e:
        print(json.dumps({"compile_error": f"{type(e).__name__}: {e}", "results": []}))
        return
    for t in tests:
        try:
            got = fn(*t["args"])
            results.append({"args": t["args"], "expected": t["expected"], "got": got,
                            "passed": got == t["expected"]})
        except Exception as e:
            results.append({"args": t["args"], "expected": t["expected"], "got": None,
                            "passed": False, "error": f"{type(e).__name__}: {e}"})
    print(json.dumps({"compile_error": None, "results": results}))

if __name__ == "__main__":
    main()
