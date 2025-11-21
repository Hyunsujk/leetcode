class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(start, slate, total):
            if total == target:
                res.append(slate[:])
                return
            
            if total > target or start == len(candidates):
                return
            
            slate.append(candidates[start])
            helper(start, slate, total + candidates[start])
            slate.pop()
            helper(start+1, slate, total)
        
        helper(0, [], 0)
        return res