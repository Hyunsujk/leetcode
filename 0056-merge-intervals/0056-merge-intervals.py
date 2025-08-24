class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        intervals.sort(key=lambda x: (x[0], x[1]))

        for interval in intervals:
            if merged and interval[0] <= merged[-1][1]:
                merged[-1][1] = max(interval[1], merged[-1][1])
            else:
                merged.append(interval)
        
        return merged
        