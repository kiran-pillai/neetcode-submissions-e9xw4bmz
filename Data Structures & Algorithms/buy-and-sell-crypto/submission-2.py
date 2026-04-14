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
        l, r = 0, 1
        profit=0
        while r<len(prices):
            current_profit=prices[r] - prices[l]
            if current_profit>0:
                profit=max(current_profit,profit)
            if prices[r]<prices[l]:
                l+=1
            if prices[r]>=prices[l]:
                r+=1
        return profit

