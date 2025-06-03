class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            sell = prices[len(prices) - i - 1] 
            buy = sell
            for j in range(len(prices) - i):
                if prices[j] < buy:
                    buy = prices[j]

            if sell - buy > max_profit:
                max_profit = sell - buy
            
        return max_profit