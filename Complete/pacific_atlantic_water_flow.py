class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        rows = len(heights)
        cols = len(heights[0])


        def dfs(r, c, ocean, prev_h):
            if (r, c) in ocean or prev_h > heights[r][c]:
                return
            else:
                ocean.add((r,c))

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if 0 <= r + dr < rows and 0 <= c + dc < cols:
                    dfs(r + dr, c + dc, ocean, heights[r][c])
        
        # we start from the outside cells
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])
        
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res

        
            