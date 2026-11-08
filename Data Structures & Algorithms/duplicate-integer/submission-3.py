class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #  output = self.has_duplicate_hash_set(nums)
         output = self.has_duplicate_brute_force(nums)
         return output
    
    def has_duplicate_brute_force(self, nums: List[int]) -> bool:
        '''O(n^2) time complexity''' 
        output = False
        for i in range(len(nums)):
            output = output or nums[i] in nums[-1:i:-1]

        return output

    def has_duplicate_hash_set(self, nums: List[int]) -> bool:
        '''O(n) time complexity'''
        return len(set(nums)) < len(nums)