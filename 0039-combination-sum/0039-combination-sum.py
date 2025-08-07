class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def build_combination(start, slate, total):
            if total == target:
                res.append(slate[:])
                return
            if total > target:
                return 
            for i in range(start, len(candidates)):
                slate.append(candidates[i])
                build_combination(i, slate, total + candidates[i])
                slate.pop()
        
        build_combination(0, [], 0)
        return res