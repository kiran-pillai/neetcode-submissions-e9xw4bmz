"""
[0,0,0,0,0,0,0,0,0,0,0,0]
[0,1,2,3,4,1,2,3,4,5,1,2]
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [float('inf')] * (amount + 1 )
        dp[0] = 0
        for i in range(1, len(dp)):
            for coin in coins:
                if i // coin >= 1:
                    dp[i] = min(
                        dp[i],dp[i-coin] + 1
                    )
        return -1 if dp[-1] == float('inf') else dp[-1]
