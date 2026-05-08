class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for key, value in f.items():
            buckets[value].append(key)
        buckets = list(reversed([b for b in buckets if b]))
        buckets = [l for ls in buckets for l in ls]
        return buckets[0:k]
