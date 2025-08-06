class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:      
        seen = []
        left = 0
        right = 0
        length = 0
        while right < len(s):
            if s[right] in seen:
                length = max(length, len(seen))
                left += 1
            else:
                seen.append(s[right])
            right += 1
        length = max(length, len(seen))
        return length