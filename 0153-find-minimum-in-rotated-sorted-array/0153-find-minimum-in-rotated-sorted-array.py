class Solution:
    def findMin(self, nums: List[int]) -> int:
        def helper(start,end):
            if start == end:
                return nums[start]
            mid = (end+start)//2
            if nums[mid] > nums[end]:
                return helper(mid+1, end)
            else:
                return helper(start, mid)
        
        return helper(0, len(nums)-1)