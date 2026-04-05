class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy_point, i = self.findBuyPoint(prices, 0)
        max_profit = 0
        sell_point = 0
        i = 0
        while i < len(prices):
            buy_point, i = self.findBuyPoint(prices, i)
            print(buy_point, i)
            sell_point, i = self.findSellPoint(prices, i)
            print(sell_point, i)
            if sell_point == -1: break
            max_profit += sell_point - buy_point
            print(max_profit, i)
        return max_profit
            
    def findBuyPoint(self, prices, i):
        buy_point = prices[i]
        i += 1
        while i < len(prices) and prices[i] <= prices[i - 1]:
            buy_point = prices[i]
            i += 1
        return buy_point, i

    def findSellPoint(self, prices, i):
        sell_point = -1
        while i < len(prices) and prices[i] >= prices[i - 1]:
            sell_point = prices[i]
            i += 1
        return sell_point, i
        
