class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         output = self.has_duplicate_hash_map(nums)
         return output
    
    def has_duplicate_hash_map(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)