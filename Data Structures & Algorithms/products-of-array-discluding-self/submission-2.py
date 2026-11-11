from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0]*len(nums)
        
        if nums.count(0) == 1:
            zero_index = nums.index(0)
            nums_copy = nums.copy()
            nums_copy[zero_index] = 1
            product = prod(nums_copy)
            output = [0] * zero_index + [product] + [0] * (len(nums_copy) - zero_index -1)
            return output
        
        product = prod(nums)
        output = [int(product/num) for num in nums]
        return output