class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return '[]'
        return '%%%'.join(strs)
    def decode(self, s: str) -> List[str]:
        output = s.split('%%%') if s != '[]' else []
        return output