class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set(nums)
        max_len = 0
        for item in seen:
            if item - 1 not in seen:
                length = 1
                while item + length in seen:
                    length += 1
                max_len = max(max_len, length)
        return max_len