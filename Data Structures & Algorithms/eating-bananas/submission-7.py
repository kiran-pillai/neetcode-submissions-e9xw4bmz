import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_h=r
        while l<=r:
            total_time=0
            k= (l + r) // 2
            for num in piles:
                total_time+=math.ceil(num/k)
                if total_time>h:
                    break
            if total_time<=h:
                min_h=min(min_h,k)
                r = k - 1 
            else:
                l = k + 1
        return min_h