"""
Brute force: 
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        maxx = float('-inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                print(nums[i:j+1])
                maxx = max(maxx, math.prod(nums[i:j+1]))
        return maxx
"""

"""
nums=[1,2,-3,4]
[-inf, -inf, -inf, -inf]

"""

import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        minn, maxx = 1, 1
        for num in nums:
            temp = num * maxx
            maxx = max(num*minn, temp, num)
            minn = min(num*minn, temp, num) 
            res = max(maxx, res)
        return res
                
        