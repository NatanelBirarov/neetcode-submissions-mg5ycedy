class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max_profit = 0
        while j < len(prices):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
            if prices[i] > prices[j]:
                i = j
            j += 1
        return max_profit