class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for idx, num in enumerate(nums):
            need = target - num
            if need in m:
                return sorted([m[need], idx])
            m[num] = idx