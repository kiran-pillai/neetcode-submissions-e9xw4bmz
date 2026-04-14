class Solution:
    """
    Naive
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_array=sorted(nums)
        lis=[]
        for i in range(len(sorted_array)):
            for j in range(i+1,len(sorted_array)):
                for k in range(j+1,len(sorted_array)):
                    sum=sorted_array[i]+sorted_array[j]+sorted_array[k]
                    new_array=[sorted_array[i],sorted_array[j],sorted_array[k]]
                    if sum==0 and new_array not in lis:
                        lis.append(new_array)
        return lis
