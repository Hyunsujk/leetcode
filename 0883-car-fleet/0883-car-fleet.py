class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        time = []

        for i in range(len(position)):
            t = (target-position[i])/speed[i]
            time.append((position[i], t))
        
        time.sort(key=lambda x:x[0], reverse=True)

        for p, t in time:
            if not fleet or fleet[-1] < t:
                fleet.append(t)
        
        return len(fleet)