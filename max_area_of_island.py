class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_size = 0
        max_island = 0

        def dfs(r, c):
            nonlocal island_size

            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
            island_size += 1
            grid[r][c] = 0

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if ((nr) in range(rows) and 
                    (nc) in range(cols) and
                    grid[nr][nc] == 1):
                    grid[nr][nc] = 0
                    dfs(nr, nc)



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    island_size = 0
                    dfs(r, c) # a new island
                    max_island = max(max_island, island_size)

        return max_island