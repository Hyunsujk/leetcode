class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i in range(len(heights)+1):
            curr_height = heights[i] if i < len(heights) else 0
            while stack and heights[stack[-1]] > curr_height:
                rec_right = i
                rec_height = heights[stack.pop()]
                rec_left = stack[-1] if stack else -1
                area = (rec_right - rec_left - 1) * rec_height
                max_area = max(max_area, area)
            stack.append(i)
        return max_area