from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = self.top_k_frequent_sorting(nums, k)
        return output
        
    def top_k_frequent_sorting(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        counter_sorted = list(counter.items())
        counter_sorted.sort(key=lambda a: a[1], reverse=True)
        k_elem = [counter[0] for counter in counter_sorted[0:k]]
        return k_elem