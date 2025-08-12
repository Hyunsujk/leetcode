class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPal(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        
        res = 0
        for i in range(len(s)):
            res += isPal(i, i+1)
            res += isPal(i, i)

        return res

        