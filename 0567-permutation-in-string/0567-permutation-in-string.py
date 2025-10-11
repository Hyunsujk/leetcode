class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        
        left = 0
        right = len(s1) - 1

        while right < len(s2):
            if s2[left] in s1:
                sub_count = Counter(s2[left:right+1])
                if s1_count == sub_count:
                    return True
            left += 1
            right += 1
        
        return False
                
        