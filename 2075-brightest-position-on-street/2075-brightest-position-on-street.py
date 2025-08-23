class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        brightness_change = defaultdict(int)
        for p, r in lights:
            brightness_change[p-r] += 1
            brightness_change[p+r+1] -= 1
        
        brightness = 0
        max_brightness = 0
        max_idx = 0

        for i, b in sorted(brightness_change.items()):
            brightness += b
            if brightness > max_brightness:
                max_brightness, max_idx = brightness, i
        
        return max_idx
    

        