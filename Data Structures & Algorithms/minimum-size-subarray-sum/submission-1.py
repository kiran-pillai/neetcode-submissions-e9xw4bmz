class Solution:
    """
    Initialize l and r to 0
    Iterate through the whole array o(n)
    if the currSum>=target -> update length, takeaway 
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length=float("inf")
        l, currSum=0, 0
        for r,num in enumerate(nums):
            currSum+=num
            while currSum>=target:
                length = min((r-l)+1, length)
                currSum-=nums[l]
                l+=1
        return 0 if length==float("inf") else length