class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        track = []

        maxArea = 0
        for r, h in enumerate(chain([0],heights,[0])):
            if track and track[-1][1] > h:
                while track[-1][1] > h:
                    curr = track.pop()
                    height = curr[1]
                    width = r - track[-1][0] -1
                    area = height * width
                    maxArea = max(maxArea, area)
            track.append((r, h))
        
        return maxArea
            

        