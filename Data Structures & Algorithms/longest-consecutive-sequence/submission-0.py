from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        counter = Counter(nums)
        min_num = min(nums)
        max_num = max(nums)
        max_len = 0
        
        length = 0
        while min_num <= max_num:
            if min_num not in counter:
                length = 0
            length +=  min_num in counter
            min_num += 1
            max_len = max(length, max_len)


        return max_len
