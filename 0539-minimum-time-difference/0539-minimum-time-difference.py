class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        ordered = [(int(t[0:2]), int(t[3:5])) for t in timePoints]
        noDups = set(ordered)
        if len(noDups) < len(ordered):
            return 0
 
        ordered.sort(key = lambda x: (x[0], x[1]))
        minDiff = float("inf")
        minList = [ h*60 + m for (h,m) in ordered]

        for i in range(1, len(minList)):
            minDiff = min(minDiff, minList[i] - minList[i-1])
        
        minDiff = min(minDiff, 24*60 - (minList[-1] - minList[0]))

        return minDiff

        