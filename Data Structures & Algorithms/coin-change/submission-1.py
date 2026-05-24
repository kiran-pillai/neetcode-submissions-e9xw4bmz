class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount+1)  
        dp[0] = 0  
        for i in range(1,amount+1):
            vals = []
            for coin in coins:
                if i - coin>=0:
                    vals.append(dp[i-coin] + 1)
                else:
                    vals.append(amount + 1)
            dp[i] = min(vals)
        print(dp)
        return -1 if dp[-1] >= amount + 1 else dp[-1]