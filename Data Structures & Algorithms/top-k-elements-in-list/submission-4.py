from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        items_sorted = sorted(counter.items(), key=lambda x: x[1])
        # print(f"{items_sorted=}")
        # print(items_sorted[-1:-k-1:-1])
        return [item[0] for item in items_sorted[-1:-k-1:-1]]
        