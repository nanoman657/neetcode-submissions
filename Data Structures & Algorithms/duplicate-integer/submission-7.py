from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for key, value in counter.items():
            if value > 1:
                return True
        return False