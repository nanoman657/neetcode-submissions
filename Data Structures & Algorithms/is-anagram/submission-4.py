from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)

        anagram = counter_s == counter_t
        return anagram