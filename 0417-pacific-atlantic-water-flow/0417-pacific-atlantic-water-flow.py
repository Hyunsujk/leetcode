class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_height):
            if (r,c) in visited or heights[r][c] < prev_height:
                return

            visited.add((r,c))

            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc, visited, heights[r][c])
            
        
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])
        
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])
        
        return list(map(list, pacific & atlantic))