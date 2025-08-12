class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0

        def isPal(l, r):
            if l < 0 or r >= len(s) or s[l] != s[r]:
                return
            self.count += 1
            return isPal(l-1, r+1)
        
        for i in range(len(s)):
            isPal(i, i+1)
            isPal(i, i)

        return self.count

        