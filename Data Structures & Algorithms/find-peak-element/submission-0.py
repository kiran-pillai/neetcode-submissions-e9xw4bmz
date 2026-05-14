class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxx = (float('-inf'), float('-inf'))
        for i, num in enumerate(nums):
            if num>maxx[1]:
                maxx = (i, num)
        return maxx[0]