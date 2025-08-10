class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(pos):
            r = pos[0]
            c = pos[1]

            if pos == (m-1, n-1):
                return 1
            
            if pos in memo:
                return memo[pos]

            paths = 0
            for i, j in [(1,0), (0,1)]:
                if r+i < m and c+j < n:
                    paths += dfs((r+i, c+j))
            
            memo[pos] = paths

            return paths

        return dfs((0,0))