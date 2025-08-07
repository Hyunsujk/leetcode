class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)]]*2

        for i in range(1, m):
            for j in range(1, len(dp[0])):
                row = m % 2
                other_row = 0 if row == 1 else 1
                dp[row][j] = dp[other_row][j] + dp[row][j-1]
            
            temp = dp[0]
            dp[0] = dp[1]
            dp[1] = temp
            

        return dp[0][n-1]


        