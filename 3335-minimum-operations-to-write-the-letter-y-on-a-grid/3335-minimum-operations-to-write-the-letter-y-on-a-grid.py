class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = n // 2

        ypos = set()
        for i in range(m):
            ypos.add((i,i))
            ypos.add((i, n-1-i))
        for i in range(m, n):
            ypos.add((i, m))
        
        ycount = [0, 0, 0]
        bcount = [0, 0, 0]
        for x in range(n):
            for y in range(n):
                if (x, y) in ypos:
                    ycount[grid[x][y]] += 1
                else:
                    bcount[grid[x][y]] += 1
        
        ytotal = len(ypos)
        btotal = n*n - ytotal
        
        change = float("inf")
        for ycolor in range(3):
            for bcolor in range(3):
                if ycolor == bcolor:
                    continue
                ychange = ytotal - ycount[ycolor]
                bchange = btotal - bcount[bcolor]

                change = min(change, ychange + bchange)
        
        return change


        