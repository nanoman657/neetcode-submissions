from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.is_anagram_hash_map(s,t)
        
    def is_anagram_hash_map(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)        