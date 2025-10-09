class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        track = []
        res = [0] * n

        for i in range(n):
            while track and temperatures[track[-1]] < temperatures[i]:
                prev = track.pop()
                res[prev] = i - prev
            track.append(i)
        
        return res