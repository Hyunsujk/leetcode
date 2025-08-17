class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            height_l = height[left]
            height_r = height[right]
            h = min(height_l, height_r)
            area = width * h
            max_area = max(max_area, area)
            if height_l < height_r:
                left += 1
            elif height_r < height_l:
                right -= 1
            else:
                left += 1
                right -= 1
            
        return max_area