from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashes = [hash(tuple(sorted(string))) for string in strs]
        str_map = {}
        for i in range(len(strs)):
            print(str_map)
            str_map[hashes[i]] = str_map.get(hashes[i], []) + [strs[i]]
        return list(str_map.values())