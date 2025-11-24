class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            area = 1

            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr = dr + r
                nc = dc + c
                area += dfs(nr, nc)
            
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area