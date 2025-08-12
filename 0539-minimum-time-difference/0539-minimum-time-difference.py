class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minList = []
        for t in timePoints:
            h = int(t[0:2])
            m = int(t[3:5])
            minList.append(h*60 + m)
        
        minList.sort()
        minDiff = float("inf")

        for i in range(1, len(minList)):
            minDiff = min(minDiff, minList[i] - minList[i-1])
        
        minDiff = min(minDiff, 24*60 - (minList[-1] - minList[0]))

        return minDiff

        