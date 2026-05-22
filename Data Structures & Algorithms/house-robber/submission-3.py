class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = []
        for i, num in enumerate(nums):
            if i == 0:
                dp.append(num)
            elif i == 1:
                dp.append(max(dp[i-1], num))
            else:
                dp.append(max(num+dp[i-2], dp[i-1]))
        return dp[-1]