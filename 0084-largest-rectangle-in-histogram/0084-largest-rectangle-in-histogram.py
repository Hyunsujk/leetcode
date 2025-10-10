class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for r, height in enumerate(chain([0],heights,[0])):
            if stack and stack[-1][1] > height:
                while stack and stack[-1][1] > height:
                    l = stack.pop()
                    w = r - stack[-1][0] -1
                    a = w * l[1]
                    maxArea = max(maxArea, a)
            stack.append([r, height])
 
        return maxArea
