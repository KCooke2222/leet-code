class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        memo = [[-1] * n for _ in range(m)]

        def dfs(r, c):
            if c == len(t):
                return 1
            if r == len(s):
                return 0
            
            if memo[r][c] != -1:
                return memo[r][c]

            res = dfs(r + 1, c)
            if s[r] == t[c]:
                res += dfs(r + 1, c + 1)
            
            memo[r][c] = res
            return res

        return dfs(0, 0)