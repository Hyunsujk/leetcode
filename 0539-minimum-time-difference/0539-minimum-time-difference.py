class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(set(timePoints)) < len(timePoints):
            return 0
        
        minutes = []
        for t in timePoints:
            hour = int(t[:2])
            minute = int(t[3:])
            minutes.append(hour * 60 + minute)
        
        minutes.sort()
        print(minutes)

        minDiff = 24*60
        for i in range(1, len(minutes)):
            if minutes[i] - minutes[i-1] < minDiff:
                minDiff = minutes[i] - minutes[i-1]
        
        minDiff = min(minDiff, (24*60 - (minutes[-1] - minutes[0])))

        return minDiff

        