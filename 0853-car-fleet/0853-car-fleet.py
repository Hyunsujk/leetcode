class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        fleet = []

        for i in range(len(position)):
            time_taken = (target-position[i]) / speed[i]
            time.append((position[i], time_taken))

        time.sort(key=lambda x: x[0], reverse=True)
        
        for position, time_taken in time:
            if not fleet or fleet[-1] < time_taken:
                fleet.append(time_taken)

        return len(fleet)