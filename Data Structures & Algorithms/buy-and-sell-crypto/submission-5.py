class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_so_far = prices[0]
        max_profit = 0
        for i in range(n):
            min_so_far = min(min_so_far, prices[i])
            curr_profit = prices[i] - min_so_far
            max_profit = max(max_profit, curr_profit)
        return max_profit