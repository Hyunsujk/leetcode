class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        if n <= 1:
            return n

        def expand(l, r):
            c = 0
            while l >= 0 and r < n and s[l] == s[r]:
                c += 1
                l -= 1
                r += 1
            return c
        
        count = 0
        for i in range(n):
            count += expand(i, i)
            count += expand(i, i+1)
        
        return count