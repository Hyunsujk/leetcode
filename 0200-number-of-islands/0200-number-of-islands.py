class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0        

        def helper(x,y):
            if x >= rows or x < 0 or y >= cols or y < 0 or grid[x][y] != "1":
                return

            grid[x][y] = "-1"
            helper(x+1, y)
            helper(x-1, y)
            helper(x, y-1)
            helper(x, y+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    helper(r, c)

        return count
                
        