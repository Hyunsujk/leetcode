class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(openn, close, s):
            if len(s) == n * 2:
                res.append(s)
                return
            
            if openn < n:
                dfs(openn+1, close, s+"(")
            
            if close < openn:
                dfs(openn, close+1, s+")")
            
        dfs(0, 0, "")

        return res