class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(set(timePoints)) < len(timePoints):
            return 0
        
        for i in range(len(timePoints)):
            time = timePoints[i]
            hour = int(time[0:2])
            minute = int(time[3:5])

            minutes = hour * 60 + minute
            timePoints[i] = minutes
        
        timePoints.sort()
        minDiff = float("inf")
        for i in range(1, len(timePoints)):
            diff = timePoints[i] - timePoints[i-1]
            minDiff = min(minDiff, diff)
        
        minDiff = min(minDiff, 24 * 60 - (timePoints[-1] - timePoints[0]))

        return minDiff
