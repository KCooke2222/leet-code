class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, total):
            if total == amount:  # found a valid combination
                return 1
            if total > amount or i == len(coins):  # exceeded or ran out of coins
                return 0
                
            if (i, total) in memo:
                return memo[(i, total)]

            ways = 0
            # pick coin i
            ways += dfs(i, total + coins[i])

            # skip to i + 1
            ways += dfs(i + 1, total)

            memo[(i, total)] = ways

            return ways

        return dfs(0, 0)
