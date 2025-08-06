class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]
        
        substring = ""
        length = 0
        for i in range(len(s)):
            even = expand_from_center(i, i+1)
            odd = expand_from_center(i, i)

            longer_str = even if len(even) > len(odd) else odd
            if len(longer_str) > length:
                length = len(longer_str)
                substring = longer_str
        return substring