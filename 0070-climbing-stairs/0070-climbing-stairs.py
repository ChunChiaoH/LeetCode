class Solution:
    def climbStairs(self, n: int) -> int:
        # action space: [1, 2]
        # current state: dp, number of ways from current position
        
        # range(n+2) to handle situation where n<=2
        dp = [0 for _ in range(n+2)]
        dp[1] = 1
        dp[2] = 2
        if n <= 2:
            return dp[n]
        for i in range(3, n+1):
            for a in [1, 2]:
                dp[i] += dp[i-a]
        return dp[n]