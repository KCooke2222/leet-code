class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, stock):
            if i > len(prices) - 1:
                return 0

            if (i,stock) in memo:
                return memo[(i, stock)]

            
            # do nothing
            nothing = dfs(i+1, stock)

            # buy
            if not stock:
                buy = dfs(i+1, True) - prices[i]
                memo[(i, stock)] = max(nothing, buy)

            # sell
            if stock:
                sell = dfs(i+2, False) + prices[i]
                memo[(i, stock)] = max(nothing, sell)

            return memo[(i, stock)]

        
        return dfs(0, False)  

            
