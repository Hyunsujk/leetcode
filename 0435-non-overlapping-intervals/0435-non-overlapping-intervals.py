class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        count = 0
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] >= prevEnd:
                prevEnd = curr[1]
            else:
                if prevEnd < curr[1]:
                    count += 1
                else:
                    count += 1
                    prevEnd = curr[1]
        
        return count
        