class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def island(r, c):
            grid[r][c] = "0"
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    island(nr, nc)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island(r, c)
                    count += 1
    
        
        return count
