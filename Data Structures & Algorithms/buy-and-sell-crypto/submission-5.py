"""
intialize l=0 and r = 1
initialize profit = float("-inf")

When do we increment l? 
- l>r
When do we increment r?
- r>=l

What is the end condition?
- r == len(prices)-1


"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
    
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(profit, max_profit)
        return max_profit


