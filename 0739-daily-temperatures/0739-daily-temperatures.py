class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        track = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while track and track[-1][1] < temp:
                prev = track.pop()
                res[prev[0]] = i - prev[0]
            track.append((i, temp))
        
        return res