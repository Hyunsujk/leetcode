class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, height in enumerate(chain([0],heights,[0])):
            while stack and stack[-1][1] > height:
                rec_right = i
                rec_height = stack.pop()[1]
                rec_left = stack[-1][0]
                area = (rec_right - rec_left - 1) * rec_height
                max_area = max(max_area, area)
            stack.append((i, height))
        return max_area