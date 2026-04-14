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
   
        if len(prices) ==1:
            return 0

        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
        return max_profit

