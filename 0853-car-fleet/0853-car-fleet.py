class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        cars = sorted(zip(position,speed), reverse=True)

        for position, speed in cars:
            time_taken = (target-position) / speed
            if not stack or stack[-1] < time_taken:
                stack.append(time_taken)
        
        return len(stack)