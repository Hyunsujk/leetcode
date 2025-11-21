class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        
        def helper(i, slate):
            if i == len(nums):
                self.res.append(slate[:])
                return
            
            slate.append(nums[i])
            helper(i+1, slate)
            slate.pop()
            helper(i+1, slate)
        
        helper(0, [])
        return self.res