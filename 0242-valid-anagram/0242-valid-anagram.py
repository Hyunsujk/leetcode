class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_char = set(s)
        for char in s_char:
            if s.count(char) != t.count(char):
                return False
        return True