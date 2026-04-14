import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        print(nums)
        median=(len(nums)-1)/2
        if len(nums)==1:
            return nums[0]
        elif median.is_integer():
            return nums[int(median)]
        else:
            lower=math.floor(median)
            upper=math.ceil(median)
            final=(nums[lower]+nums[upper])/2
            return final

            