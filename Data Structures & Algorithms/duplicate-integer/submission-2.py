class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #  output = self.has_duplicate_hash_map(nums)
         output = self.has_duplicate_brute_force(nums)
         return output
    
    def has_duplicate_brute_force(self, nums: List[int]) -> bool:
        output = False
        for i in range(len(nums)):
            output = output or nums[i] in nums[-1:i:-1]

        return output

    def has_duplicate_hash_map(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)