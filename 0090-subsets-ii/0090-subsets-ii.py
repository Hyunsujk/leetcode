class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def helper(start, slate):
            res.append(slate[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                slate.append(nums[i])
                helper(i+1, slate)
                slate.pop()
        
        helper(0, [])
        return res