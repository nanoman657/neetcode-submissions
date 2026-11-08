class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tuples = [tuple(sorted(string)) for string in strs]
        str_map = {}

        for i in range(len(strs)):
            str_map[tuples[i]] = str_map.get(tuples[i], []) + [strs[i]]
        return list(str_map.values())