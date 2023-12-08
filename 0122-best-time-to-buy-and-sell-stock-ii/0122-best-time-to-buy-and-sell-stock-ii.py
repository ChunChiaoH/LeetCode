class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        dp = [0 for _ in prices]
        dp[-1] = 0
        dp[-2] = max(0, prices[-1] - prices[-2])
        
        max_price = max(prices[-1], prices[-2])
        profit = 0
        idxs = [i for i in range(len(prices)-2)][::-1]
        for idx, p in zip(idxs, prices[::-1][2:]):
            #dp[idx] = max(prices[idx+1]-prices[idx], 0) + dp[idx+1]
            max_price = max(p, max_price)
            dp[idx] = max(p-max_price, max(prices[idx+1]-prices[idx], 0) + dp[idx+1])
            
        return dp[0]