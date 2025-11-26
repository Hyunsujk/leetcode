class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            
            return s[l+1:r]

        longest = ""
        for i in range(n):
            even = expand(i, i+1)
            odd = expand(i, i)

            longer = even if len(even) > len(odd) else odd

            if len(longer) > len(longest):
                longest = longer

        return longest