class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if self.find_string(i, j, board, word, 0):
                        return True
        
        return False
    
    def find_string(self, row, col, board, word, i):
        if i == len(word):
            return True
        
        if (row < 0 or row >= len(board) 
        or col < 0 or col >= len(board[0]) 
        or board[row][col] != word[i]):
            return False

        temp = board[row][col]
        board[row][col] = "#"

        found = (
            self.find_string(row+1, col, board, word, i+1) or
            self.find_string(row-1, col, board, word, i+1) or
            self.find_string(row, col+1, board, word, i+1) or
            self.find_string(row, col-1, board, word, i+1)
        )

        board[row][col] = temp
        
        return found