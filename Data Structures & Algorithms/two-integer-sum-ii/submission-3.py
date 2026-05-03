class Solution:
    """
    Options:
    - prefix sum
    - Two pointers
    - 
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r=len(numbers)-1
        l=0
        while l<r:
            right = numbers[r]
            left = numbers[l]
            if right+left == target:
                return [l+1,r+1]
            elif right+left<target:
                l+=1
            else:
                r-=1
        return False