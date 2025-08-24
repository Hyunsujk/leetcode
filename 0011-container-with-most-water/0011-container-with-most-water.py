class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        maxArea = 0
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            a = h * w
            maxArea = max(maxArea, a)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        
        return maxArea
        