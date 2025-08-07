class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            curr = res[-1]
            if intervals[i][0] <= curr[1]:
                res[-1][1] = max(curr[1], intervals[i][1])
            else:
                res.append(intervals[i])
        
        return res