from functools import reduce
from copy import copy

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_array = []
        for num in nums:
            nums_copy = copy(nums)
            nums_copy.remove(num)
            product = reduce(lambda a, b: a*b, nums_copy)
            product_array.append(product)
        
        return product_array