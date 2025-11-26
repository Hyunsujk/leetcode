class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(dp)):
            one = int(s[i-1])
            two = int(s[i-2:i])

            if one != 0:
                dp[i] += dp[i-1]
            if 10 <= two < 27:
                dp[i] += dp[i-2]
        
        return dp[-1]
