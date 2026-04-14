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
            left_pointer=numbers[l]
            right_pointer=numbers[r]
            sum=left_pointer+right_pointer
            if sum==target:
                return [l+1,r+1]
            elif sum<target:
                l+=1
            elif sum>target:
                r-=1
        return False