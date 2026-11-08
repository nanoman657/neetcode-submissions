delimiter = '\t&'
empty = 'null&'

class Solution:    
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return empty
        return delimiter.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == empty:
            return []
        return s.split(delimiter)