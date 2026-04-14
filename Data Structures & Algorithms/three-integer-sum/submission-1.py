class Solution:
    """
    Naive 
    """
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     sorted_array=sorted(nums)
    #     lis=[]
    #     for i in range(len(sorted_array)):
    #         for j in range(i+1,len(sorted_array)):
    #             for k in range(j+1,len(sorted_array)):
    #                 print({"i":i,"j":j,"k":k})
    #                 sum=sorted_array[i]+sorted_array[j]+sorted_array[k]
    #                 new_array=[sorted_array[i],sorted_array[j],sorted_array[k]]
    #                 if sum==0 and new_array not in lis:
    #                     lis.append(new_array)
    #     return lis

    """
    Iterate one by one and then use two sum to "squeeze" second and third values
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue

            low, high = i+1, len(nums)-1
            while low < high:
                sum=nums[low] + nums[high] + nums[i]
                if sum == 0:
                    res.append([nums[low], nums[high], nums[i]])
                    low, high = low + 1, high - 1
                    while nums[low] == nums[low - 1] and low < high:
                        low+=1
                elif sum < 0:
                    low+=1
                elif sum > 0:
                    high-=1
        return res