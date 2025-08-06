class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while right > left:
            right_height = height[right]
            left_height = height[left]
            width = right - left
            h = min(right_height, left_height)
            area = width * h
            max_area = max(max_area, area)
            if right_height > left_height:
                left += 1
            else:
                right -= 1
        return max_area

        