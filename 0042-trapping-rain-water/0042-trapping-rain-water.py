class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        area = 0

        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                mid = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                width = i - left - 1
                water_height = min(height[left], h) - height[mid]
                area += width * water_height
            stack.append(i)
        
        return area