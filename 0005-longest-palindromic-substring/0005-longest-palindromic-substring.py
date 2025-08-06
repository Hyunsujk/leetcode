class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        sub_str = ""

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1: right]

        for i in range(len(s)-1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i+1)
            
            if len(odd) > len(sub_str):
                sub_str = odd
            if len(even) > len(sub_str):
                sub_str = even
        
        return sub_str