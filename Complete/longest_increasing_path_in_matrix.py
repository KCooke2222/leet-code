class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = [[-1] * n for _ in range(m)]

        def dfs(r, c):
            if memo[r][c] != -1:
                return memo[r][c]

            longest = 1
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if matrix[r][c] < matrix[nr][nc]:
                        longest = max(longest, 1 + dfs(nr, nc))
                
            memo[r][c] = longest
            return longest

        longest = 1
        for r in range(m):
            for c in range(n):
                longest = max(longest, dfs(r, c))
        
        return longest
