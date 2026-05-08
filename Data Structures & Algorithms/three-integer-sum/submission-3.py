class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        triplets = set()
        i = 0
        while nums[i] <= 0 and i < n - 2:
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    triplets.add((nums[i], nums[l], nums[r]))
                    l +=1 ; r -= 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
            i += 1
        return [[i, j, k] for i, j, k in triplets]     



        