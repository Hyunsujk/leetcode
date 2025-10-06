class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = [char for char in s]
        tl = [char for char in t]
        return sorted(sl) == sorted(tl)