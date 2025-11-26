class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            
            return s[l+1:r]
        
        if n == 0:
            return 0
        if n == 1:
            return s

        longest = ""
        for i in range(1, n):
            even = expand(i-1, i)
            odd = expand(i, i)

            longer = even if len(even) > len(odd) else odd

            if len(longer) > len(longest):
                longest = longer

        return longest