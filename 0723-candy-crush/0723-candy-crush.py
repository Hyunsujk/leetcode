class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows = len(board)
        cols = len(board[0])

        while True:
            crush = set()
            
            for r in range(rows):
                for c in range(cols-2):
                    if board[r][c] == board[r][c+1] == board[r][c+2] != 0:
                        crush.update([(r,c), (r,c+1), (r,c+2)])
            
            for c in range(cols):
                for r in range(rows-2):
                    if board[r][c] == board[r+1][c] == board[r+2][c] != 0:
                        crush.update([(r,c), (r+1,c), (r+2,c)])
            
            if not crush:
                break
            
            for r, c in crush:
                board[r][c] = 0

            for c in range(cols):
                lowestZero = rows-1
                for r in range(rows-1,-1,-1):
                    if board[r][c] != 0:
                        board[r][c], board[lowestZero][c] = board[lowestZero][c], board[r][c]
                        lowestZero -= 1
                for r in range(lowestZero,-1,-1):
                    board[r][c] = 0

        return board



        