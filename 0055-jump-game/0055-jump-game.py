class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal_idx = len(nums)-1
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= goal_idx:
                goal_idx = i
        
        return goal_idx == 0