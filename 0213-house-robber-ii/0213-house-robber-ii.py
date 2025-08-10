class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(houses):
            if len(houses) == 1:
                return houses[0]
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                dp[i] = max(dp[i-2] + houses[i], dp[i-1])
            
            return dp[-1]
        
        if len(nums) == 1:
            return nums[0]
        
        first_house = helper(nums[:-1])
        second_house = helper(nums[1:])

        return max(first_house, second_house)        