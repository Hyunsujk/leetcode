class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def helper(start, slate, total):
            if total == target:
                res.append(slate[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                if total + candidates[i] > target:
                    break
                
                slate.append(candidates[i])
                helper(i+1, slate, total + candidates[i])
                slate.pop()

        helper(0, [], 0)
        return res