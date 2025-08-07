class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def build_combination(i, slate, total):
            if total == target:
                res.append(slate[:])
                return
                
            if i >= len(candidates) or total > target:
                return
            
            slate.append(candidates[i])
            build_combination(i, slate, total + candidates[i])
            slate.pop()
            build_combination(i+1, slate, total)

        build_combination(0, [], 0)
        return res
        