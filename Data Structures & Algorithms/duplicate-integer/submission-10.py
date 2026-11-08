class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Single Pass Hash map
        counter = dict()
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter[num] > 1: return True
        return False
