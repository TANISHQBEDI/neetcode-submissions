class Solution:
    def validSpeed(self, piles, h, k):
        total_hours = 0
        for p in piles:
            # ceil(p / k) using integer arithmetic
            total_hours += (p + k - 1) // k
        return total_hours <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r  # initialize with worst case (max speed)

        while l <= r:
            m = l + (r - l) // 2
            if self.validSpeed(piles, h, m):
                # m is feasible, try smaller
                res = min(res, m)
                r = m - 1
            else:
                # m too small
                l = m + 1

        return res