class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows = len(boxGrid)
        cols = len(boxGrid[0])

        for i in range(rows):
            lowestEmpty = cols-1
            for j in range(cols-1, -1, -1):
                if boxGrid[i][j] == "#":
                    boxGrid[i][j], boxGrid[i][lowestEmpty] = boxGrid[i][lowestEmpty], boxGrid[i][j]
                    lowestEmpty -= 1
                if boxGrid[i][j] == "*":
                    lowestEmpty = j-1
        
        res = [["."] * rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                res[c][rows-1-r] = boxGrid[r][c]
        
        return res