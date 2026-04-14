import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        keep finding the middle of the array until the subarray is <=2
        """

        
        start=0
        end=len(nums)-1
        
        while start<=end:
            middle=(end+start)//2
            middle_item=nums[middle]
            if middle_item==target:
                return middle
            elif target>middle_item:
                start=middle + 1
            elif target<middle_item:
                end=middle - 1
        return -1