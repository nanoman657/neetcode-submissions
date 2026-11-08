class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        s_list: list = list(s)
        t_list: list = list(t)

        s_list.sort()
        t_list.sort()

        for i in range(len(s_list)):
            if s_list[i] != t_list[i]:
                return False
        return True
