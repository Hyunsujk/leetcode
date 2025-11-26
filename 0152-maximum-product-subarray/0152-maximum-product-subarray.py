class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_d = nums[0]
        min_d = nums[0]
        res = nums[0]

        for i in range(1, n):
            if nums[i] < 0:
                max_d, min_d = min_d, max_d
            max_d = max(nums[i], max_d * nums[i])
            min_d = min(nums[i], min_d * nums[i])
            res = max(res, max_d)
        
        return res