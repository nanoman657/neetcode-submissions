from collections import Counter
from copy import copy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums[i+1:]:
                index = nums.index(diff, i+1)
                return [i, index]

        # [0,1,2,3]
        # [3,4,5,6]
        # counter = Counter(nums)
        # num_map2 = {}
        # for i, num in enumerate(nums):
        #     num_map2[num] = num_map2.get(num, []) + [i]
        # print(num_map2)
        # num_map = {value: index for index, value in enumerate(nums)}
        # for index, value in enumerate(nums):
        #     if num_map[value]:
        #         num_map[value].pop(index)
            
        #     pair = target-value
        #     if counter.get(pair, 0) > 0:
        #         return [index, num_map_copy[pair]]
                