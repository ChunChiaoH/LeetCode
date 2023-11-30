class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # action space: value of coins
        # current state: amount left
        
        # dp stores the least amount of coins required to the amount
        # for example, dp[1] stores the least number of coins required to amount 1
        DEFAULT_VALUE = 999999
        dp = [999999 for _ in range(amount+1)]
        
        # basic state
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                # iterate through different coins
                if i-coin >= 0:
                    # compare the coins required with previous stored number
                    dp[i] = min(dp[i], 1+dp[i-coin])
                
        return dp[amount] if dp[amount] != DEFAULT_VALUE else -1
        
        