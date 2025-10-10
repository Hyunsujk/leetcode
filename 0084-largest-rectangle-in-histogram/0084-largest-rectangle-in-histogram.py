class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        maxArea = 0

        for i, height in enumerate(chain([0],heights,[0])):
            if stack and stack[-1][1] > height:
                while stack:
                    l = stack.pop()
                    w = i - l[0]
                    a = w * l[1]
                    maxArea = max(maxArea, a)
            stack.append([i, height])

        return maxArea
