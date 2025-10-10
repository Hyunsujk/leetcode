class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(start, end):
            if start > end:
                return -1
            mid = (end + start) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return helper(start, mid-1)
            else:
                return helper(mid+1, end)
            
        return helper(0, len(nums)-1)

        