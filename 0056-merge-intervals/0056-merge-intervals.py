class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]      
        for i in range(1, len(intervals)):
            curr = res[-1]
            if curr[0] <= intervals[i][0] <= curr[1]:
                res[-1][1] = max(intervals[i][1], curr[1])
            else:
                res.append(intervals[i])
        return res
            

        