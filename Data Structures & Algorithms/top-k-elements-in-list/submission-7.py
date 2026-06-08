class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = Counter(nums)
        buckets = [[] for _ in range(n + 1)]
        for key, value in freq.items():
            buckets[value].append(key)
        buckets = [item for bucket in buckets for item in bucket if bucket][::-1]
        print(buckets)
        return buckets[:k]