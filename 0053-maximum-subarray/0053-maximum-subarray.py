class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub = nums[0]
        max_s = nums[0]

        for num in nums[1:]:
            sub = max(sub+num, num)
            max_s = max(sub, max_s)

        return max_s
            

        