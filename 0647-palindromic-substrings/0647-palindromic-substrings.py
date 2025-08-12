class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []

        def isPal(l, r):
            if l < 0 or r >= len(s) or s[l] != s[r]:
                return
            res.append(s[l:r+1])
            return isPal(l-1, r+1)
        
        for i in range(len(s)):
            isPal(i, i+1)
            isPal(i, i)

        return len(res)

        