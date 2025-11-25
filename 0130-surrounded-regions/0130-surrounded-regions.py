class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        not_surrounded = set()

        def dfs(r, c, visited):
            if (r,c) in visited:
                return 
            visited.add((r,c))

            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    dfs(nr, nc, visited)

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0, not_surrounded)
            if board[r][cols-1] == "O":
                dfs(r, cols-1, not_surrounded)
        
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c, not_surrounded)
            if board[rows-1][c] == "O":
                dfs(rows-1, c, not_surrounded)
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in not_surrounded:
                    board[r][c] = "X"