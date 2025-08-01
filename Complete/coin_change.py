class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * amount

        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')

            if memo[amount-1] != -1:
                return memo[amount-1]

            ans = float('inf')
            for coin in coins:
                res = dfs(amount - coin)
                ans = min(ans, res + 1)
            

            memo[amount-1] = ans
            
            return ans

        res = dfs(amount)
        return res if res != float('inf') else -1
         

            