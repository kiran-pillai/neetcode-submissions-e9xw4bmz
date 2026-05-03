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
        profit = 0
        min_val = float('inf')
        for num in prices:
            min_val = min(min_val, num)
            profit = max(profit, num-min_val)
            print(profit)
        return profit
