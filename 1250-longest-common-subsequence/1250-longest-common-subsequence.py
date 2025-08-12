class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        prev = [0] * (cols+1)
        curr = [0] * (cols+1)

        for r in range(1, rows+1):
            for c in range(1, cols+1):
                if text1[r-1] == text2[c-1]:
                    curr[c] = prev[c-1] + 1
                else:
                    curr[c] = max(prev[c], prev[c-1])

            prev, curr = curr, prev
            
        return prev[-1]

        
      