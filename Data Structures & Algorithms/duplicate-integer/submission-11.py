class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Single Pass Hash set
        seen = set()
        for num in nums:
            len_original = len(seen)
            seen.add(num)
            if len(seen) == len_original: return True
        return False
