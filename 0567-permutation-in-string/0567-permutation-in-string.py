class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = defaultdict(int)
        for char in s1:
            s1_count[char] += 1
        
        left = 0
        right = len(s1) - 1

        while right < len(s2):
            if s2[left] in s1:
                sub_count = defaultdict(int)
                for i in range(left, right+1):
                    sub_count[s2[i]] += 1
                if s1_count == sub_count:
                    return True
            left += 1
            right += 1
        
        return False
                
        