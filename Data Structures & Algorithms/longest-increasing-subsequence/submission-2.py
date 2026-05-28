class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]
        for i in range(1,len(nums)):
            maxxSeq = 1
            for j in range(i):
                if nums[i]>nums[j]:
                    maxxSeq = max(maxxSeq, dp[j] + 1)
            dp.append(maxxSeq)
        return max(dp)