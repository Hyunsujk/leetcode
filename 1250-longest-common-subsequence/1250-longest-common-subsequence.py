class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        dp = [[0] * (cols+1) for _ in range(rows+1)]

        for r in range(1, rows+1):
            for c in range(1, cols+1):
                if text1[r-1] == text2[c-1]:
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        
        r = rows
        c = cols
        count = 0

        while r > 0 and c > 0:
            if dp[r-1][c] == dp[r][c-1] and dp[r][c] != dp[r-1][c-1]:
                count += 1
                r -= 1
                c -= 1
            else:
                if dp[r-1][c] > dp[r][c-1]:
                    r -= 1
                else:
                    c -= 1
            
        return count

        
      