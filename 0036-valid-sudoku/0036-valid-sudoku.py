class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            filled = [n for n in board[r] if n != "."]
            if len(set(filled)) != len(filled):
                return False
        

        for c in range(cols):
            filled = [board[r][c] for r in range(rows) if board[r][c] != "."]
            if len(set(filled)) != len(filled):
                return False
            
        for r in [0, 3, 6]:
            for c in [0, 3, 6]:
                block = []
                for dr in range(3):
                    for dc in range(3):
                        nr = r + dr
                        nc = c + dc
                        block.append(board[nr][nc])
                filled = [n for n in block if n != "."]
                if len(set(filled)) != len(filled):
                    return False
        
        return True

        