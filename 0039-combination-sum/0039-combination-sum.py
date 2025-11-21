class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def helper(start, slate, total):
            if total == target:
                res.append(slate[:])
                return
            
            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    break
                slate.append(candidates[i])
                helper(i, slate, total + candidates[i])
                slate.pop()
        
        helper(0, [], 0)
        return res
