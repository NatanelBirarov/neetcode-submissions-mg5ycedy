class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_price = 0
        for price in prices:
            max_price = max(max_price, price - min_buy)
            min_buy = min(min_buy, price)
        
        return max_price
        # i, j = 0, 1
        # max_profit = 0
        # while j < len(prices):
        #     profit = prices[j] - prices[i]
        #     max_profit = max(max_profit, profit)
        #     if prices[i] > prices[j]:
        #         i = j
        #     j += 1
        # return max_profit