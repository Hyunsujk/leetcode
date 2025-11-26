class Solution:
    def countSubstrings(self, s: str) -> int:
        found = []
        n = len(s)

        if n <= 1:
            return n

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                found.append(s[l:r+1])
                l -= 1
                r += 1
        
        for i in range(n):
            expand(i, i)
            expand(i, i+1)
        
        return len(found)