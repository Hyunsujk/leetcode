class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        changes = defaultdict(int)

        for p, r in lights:
            changes[p-r] += 1
            changes[p+r+1] -= 1
        
        current_brightness = 0
        brightest_idx = 0
        brightest = float("-inf")

        for cp, c in sorted(changes.items()):
            current_brightness += c
            if current_brightness > brightest:
                brightest, brightest_idx = current_brightness, cp
        
        return brightest_idx

        