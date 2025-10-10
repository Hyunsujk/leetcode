class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(start, end):
            if start > end:
                return -1
            mid = (end+start)//2
            if nums[mid] == target:
                return mid
            
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    return helper(start, mid-1)
                else:
                    return helper(mid+1, end)
            else:
                if nums[mid] < target <= nums[end]:
                    return helper(mid+1, end)
                else:
                    return helper(start, mid-1)
        
        return helper(0, len(nums)-1)
        