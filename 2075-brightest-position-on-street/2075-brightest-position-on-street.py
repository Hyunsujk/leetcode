class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        brightness_change = defaultdict(int)

        for position, radius in lights:
            brightness_change[position - radius] += 1
            brightness_change[position + radius + 1] -= 1

        brightest_index = 0
        brightest = float("-inf")
        current_brightness = 0
            
        for curr, change in sorted(brightness_change.items()):
            current_brightness += change
            if current_brightness > brightest:
                brightest_index, brightest = curr, current_brightness
        
        return brightest_index

        