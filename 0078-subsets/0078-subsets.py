class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(start, slate):
            res.append(slate[:])

            for i in range(start, len(nums)):
                slate.append(nums[i])
                helper(i+1, slate)
                slate.pop()
        
        helper(0, [])
        return res
        