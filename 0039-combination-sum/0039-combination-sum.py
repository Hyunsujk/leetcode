class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def build_comb(start, slate, total):
            if total == target:
                res.append(slate[:])
                return
            if total > target or start >= len(candidates):
                return
            
            slate.append(candidates[start])
            build_comb(start, slate, total + candidates[start])
            slate.pop()
            build_comb(start + 1, slate, total)
        build_comb(0, [], 0)
        return res