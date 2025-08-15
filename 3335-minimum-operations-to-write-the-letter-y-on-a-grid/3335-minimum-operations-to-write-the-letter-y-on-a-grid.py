class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        center = n // 2
        ypos = set()
        ycount = [0,0,0]
        bcount = [0,0,0]
        
        for i in range(center):
            ypos.add((i,i))
            ycount[grid[i][i]] += 1
            ypos.add((i, n-1-i))
            ycount[grid[i][n-1-i]] += 1
        
        for i in range(center, n):
            ypos.add((i, center))
            ycount[grid[i][center]] += 1

        for x in range(n):
            for y in range(n):
                if (x,y) not in ypos:
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



        

        





        