class Solution:
    def climbStairs(self, n: int) -> int:
        # action space: [1, 2]
        # current state: current position
        
        dp = [0 for _ in range(n+2)]
        dp[1] = 1
        dp[2] = 2
        if n <= 2:
            return dp[n]
        #print(n+1)
        for i in range(3, n+1):
            for a in [1, 2]:
                dp[i] += dp[i-a]
        #print(dp)
        return dp[n]