// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0
        
        for k in prices:
            if k < low:
                low = k
            elif profit < (k - low):
                profit = k - low
        
        return profit
            