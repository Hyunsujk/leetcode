class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_d = nums[0]
        min_d = nums[0]
        res = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_d, min_d = min_d, max_d
            max_d = max(num, max_d * num)
            min_d = min(num, min_d * num)
            res = max(res, max_d)
        
        return res