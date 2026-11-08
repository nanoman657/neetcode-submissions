# Contains Duplicate II
# Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j with nums[i] == nums[j] and abs(i - j) <= k.
#
# Concepts: hash set as a sliding window, early exit, O(k) extra space.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # The set always holds the values from the last k indices, so a
        # duplicate in it means a repeat within distance k.
        window = set()
        for i, num in enumerate(nums):
            if num in window:
                return True          # early exit: no need to keep scanning
            window.add(num)
            if len(window) > k:      # drop the element that fell out of range
                window.remove(nums[i - k])
        return False
