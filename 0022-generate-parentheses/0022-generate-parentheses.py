class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n == 0:
            return res
        
        def helper(o, c, s):
            if len(s) == n * 2:
                res.append(s)
                return
            
            if o < n:
                helper(o+1, c, s + "(")
            if c < o:
                helper(o, c+1, s + ")")
        
        helper(0, 0, "")
        return res