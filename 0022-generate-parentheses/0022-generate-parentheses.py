class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(op, cl, s):
            if len(s) == n*2:
                res.append(s)
                return
            if op < n:
                dfs(op+1, cl, s+"(")
            
            if cl < op:
                dfs(op, cl+1, s+")")
        
        dfs(0, 0, "")
        return res