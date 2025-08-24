class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mid = n // 2
        y = set()

        for i in range(mid+1):
            y.update([(i,i), (i,n-1-i), (n-1-i, mid)])
        
        yCount = [0, 0, 0]
        notYCount = [0, 0, 0]
        for r in range(n):
            for c in range(n):
                if (r,c) in y:
                    yCount[grid[r][c]] += 1
                else:
                    notYCount[grid[r][c]] += 1
        
        changes = n*n
        ytotal = len(y)
        btotal = n*n - ytotal
        for yc in range(3):
            for bc in range(3):
                if yc == bc:
                    continue
                ychange = ytotal - yCount[yc]
                bchange = btotal - notYCount[bc]
                changes = min(changes, ychange + bchange)

        return changes



        