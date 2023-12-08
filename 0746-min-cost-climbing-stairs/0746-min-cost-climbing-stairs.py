class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [1000 for _ in range(len(cost))]
        dp[-1] = cost[-1]
        dp[-2] = min(cost[-2], cost[-2]+cost[-1]) # obviously is cost[-2]
        
        idxs = [i for i in range(len(cost))][::-1][2:]
        for idx, c in zip(idxs, cost[::-1][2:]):
            dp[idx] = c + min(dp[idx+1], dp[idx+2])
        
        return min(dp[0], dp[1])