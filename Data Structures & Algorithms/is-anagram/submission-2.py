from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # output = self.is_anagram_hash_map(s,t)
        output = self.is_anagram_sorting(s,t)
        return output

    def is_anagram_sorting(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_arr = list(s)
        t_arr = list(t)

        s_arr.sort()
        t_arr.sort()
        
        output = True
        for i in range(len(s)):
            output = output and t_arr[i] == s_arr[i]
        
        return output 
        

    def is_anagram_hash_map(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)        