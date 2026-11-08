from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_list = [(hash(str(sorted(string))), string) for string in strs]
        strs_sorted = sorted(strs, key=hash)
        seen = set()
        anagrams = []
        # print(f"{strs_sorted=}")
        
        for string in strs_sorted:
            # print(seen)
            string_hash = hash(str(sorted(string)))
            if string_hash not in seen:
                seen.add(string_hash)
                anagrams.append([string])
            else:
                for i, anagram_group in enumerate(anagrams):
                    if hash(str(sorted(anagram_group[0]))) == string_hash:
                        anagrams[i].append(string)
        # print(anagrams)
        return anagrams