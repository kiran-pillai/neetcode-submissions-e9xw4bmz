class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ%2 == 1:
            return False
        dp = set()
        dp.add(0)
        i = len(nums)-1
        while i>=0:
            newPossible = set(dp)
            for num in dp:
                newPossible.add(num+nums[i])
            dp = newPossible
            i-=1
        return summ//2 in dp