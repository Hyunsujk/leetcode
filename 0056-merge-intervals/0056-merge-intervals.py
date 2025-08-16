class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: (x[0], x[1]))

        output = [intervals[0]]

        for interval in intervals[1:]:
            latest = output[-1]
            if interval[0] <= latest[1]:
                output[-1][1] = max(interval[1], latest[1])
            else:
                output.append(interval)
        
        return output


        