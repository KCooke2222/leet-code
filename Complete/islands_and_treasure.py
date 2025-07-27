class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def bfs(start):
            visited = set()
            queue = deque([start])
            visited.add(start)

            while queue:
                cell = queue.popleft()
                i = cell[0]
                j = cell[1]
                dist = cell[2]

                if grid[i][j] > dist:
                    grid[i][j] = dist

                for d in directions:
                    ic = i + d[0]
                    jc = j + d[1]

                    if 0 <= ic < len(grid) and 0 <= jc < len(grid[0]):
                        val = grid[ic][jc]

                        if (ic, jc) not in visited and val > 0:
                            visited.add((ic, jc))
                            queue.append((ic, jc , dist + 1))


        # Iterate over the grid to find the treasure
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # BFS from treasure to whole island 
                if grid[i][j] == 0:
                    bfs((i, j, 0))


                    

