class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)
        dp1 = [0] * (len(nums) - 1)
        firstNums = nums[0:len(nums)-1]
        dp1[0] = firstNums[0]
        dp1[1] = max(firstNums[1], firstNums[0])
        for i in range(2,len(dp1)):
            dp1[i] = max(dp1[i-1], firstNums[i] + dp1[i-2])

        dp2 = [0] * (len(nums) - 1)
        secondNums = nums[1:]
        dp2[0] = secondNums[0]
        dp2[1] = max(secondNums[0],secondNums[1])
        for i in range(2,len(dp2)):
            dp2[i] = max(dp2[i-1], secondNums[i] + dp2[i-2])

        return max(dp1[-1], dp2[-1])
            