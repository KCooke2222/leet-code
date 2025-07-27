class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        
        # Get rotten fruit
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                if grid[r][c] == 1:
                    fresh += 1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        time = 0

        # run bfs
        while q:
            r, c, minute = q.popleft()
            
            time = max(time, minute)

            for d in directions:
                nr = r + d[0]
                nc = c + d[1]

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, minute + 1))


        if fresh == 0:
            return time
        else:
            return -1


        


