class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = nums[0]
        for num in nums:
            minNum=min(num, minNum)
        return minNum