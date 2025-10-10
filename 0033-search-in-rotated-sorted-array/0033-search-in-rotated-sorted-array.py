class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(start, end):
            if start == end:
                return start if nums[start] == target else -1
            mid = (end+start)//2
            if nums[mid] > nums[end] and (target > nums[mid] or target <= nums[end]):
                return helper(mid+1, end)
            else:
                return helper(start, mid)
        
        return helper(0, len(nums)-1)
        