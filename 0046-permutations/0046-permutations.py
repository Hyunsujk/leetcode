class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)

        def helper(slate):
            if len(slate) == len(nums):
                res.append(slate[:])
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                slate.append(nums[i])
                visited[i] = True
                helper(slate)
                slate.pop()
                visited[i] = False
        
        helper([])
        return res
