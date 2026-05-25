class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def findHouses(arr):
            dp = [0] * len(arr)
            for i in range(len(arr)):
                if i-2>=0:
                    dp[i] = max(dp[i-1], arr[i] + dp[i-2])
                elif i==1:
                    dp[i] = max(dp[i-1], arr[i])
                else:
                    dp[i] = arr[i]
            return dp[-1]


        return max(findHouses(nums[1:]), findHouses(nums[:-1]))



            