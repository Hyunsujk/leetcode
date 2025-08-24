class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mid = n // 2
        y = set()

        for i in range(mid+1):
            y.update([(i,i), (i,n-1-i), (n-1-i, mid)])
        
        yCount = {0:0, 1:0, 2:0}
        notYCount = {0:0, 1:0, 2:0}

        for r in range(n):
            for c in range(n):
                if (r,c) in y:
                    yCount[grid[r][c]] += 1
                else:
                    notYCount[grid[r][c]] += 1
        
        ytotal = len(y)
        y0 = ytotal - yCount[0] + min((notYCount[0]+notYCount[2]), (notYCount[0]+notYCount[1]))
        y1 = ytotal - yCount[1] + min((notYCount[1]+notYCount[0]), (notYCount[1]+notYCount[2]))
        y2 = ytotal - yCount[2] + min((notYCount[0]+notYCount[2]), (notYCount[1]+notYCount[2]))
        
        return min([y0, y1, y2])




        