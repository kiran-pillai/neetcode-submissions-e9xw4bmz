class Solution:
    """
    [1,2,1,2]
    [1,2,2,]
    """
    def __init__(self):
        self.cache = {}
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        # dp[0] = cost[0]
        # dp[1] = cost[1]
        [1,2,3,4]
        [1,2,2,]
        for i in range(2,len(dp)):
            dp[i] = min(dp[i-1]+ cost[i-1], dp[i-2] + cost[i-2])
        

        return dp[-1]