class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows = len(boxGrid)
        cols = len(boxGrid[0])

        for r in range(rows):
            lowestEmpty = cols-1
            for c in range(cols-1,-1,-1):
                if boxGrid[r][c] == "#":
                    boxGrid[r][c], boxGrid[r][lowestEmpty] = boxGrid[r][lowestEmpty], boxGrid[r][c]
                    lowestEmpty -= 1
                if boxGrid[r][c] == "*":
                    lowestEmpty = c-1
        
        res = [["."] * rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                nr = c
                nc = rows - r - 1
                res[nr][nc] = boxGrid[r][c]
        
        return res