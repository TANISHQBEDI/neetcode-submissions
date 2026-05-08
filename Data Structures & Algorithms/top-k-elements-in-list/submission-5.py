class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for key, value in f.items():
            buckets[value].append(key)
        res = []
        for b in reversed(buckets):
            res.extend(b)
            if len(res) > k:
                return res[:k]
        return res[:k]
