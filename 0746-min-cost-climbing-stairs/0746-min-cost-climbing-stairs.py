class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return 0
        if len(cost) == 2:
            return min(cost)

        dp = [0] * (len(cost)+1)
        dp[1] = cost[0]
        dp[2] = cost[1]

        for i in range(3, len(cost)+1):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i-1]
        
        return min(dp[-1], dp[-2])
