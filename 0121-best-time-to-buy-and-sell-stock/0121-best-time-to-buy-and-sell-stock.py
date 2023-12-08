class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_price = 0
        for price in prices[::-1]:
            max_price = max(max_price, price)
            profit = max(max_price-price, profit)
        return profit