class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: (x[0], x[1]))

        output = [intervals[0]]

        for i in range(1, len(intervals)):
            latest = output[-1]
            if intervals[i][0] <= latest[1]:
                output[-1][1] = max(intervals[i][1], latest[1])
            else:
                output.append(intervals[i])
        
        return output


        