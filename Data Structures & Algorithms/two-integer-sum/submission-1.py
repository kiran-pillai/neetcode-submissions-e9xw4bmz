class Solution:
    """
    iterate through each num in the array
    for each num in the array check if that num + the next num equals target
    """
    # Naive:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     length=len(nums)
    #     for i in range(length):
    #         iteratee_num=nums[i]
    #         for j in range(i+1,length):
    #             possible_match=nums[j]
    #             if (iteratee_num+possible_match==target):
    #                 return [i,j] 
    #     return False       

    # o(n)

    nums=[1,3,4,2]
    target=6


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i,num in enumerate(nums):
            map[num]=i

        for i, num in enumerate(nums):
            needed_value=target-num
            print(needed_value, map)
            if needed_value in map and map[needed_value] != i:
                return [i,map[needed_value]]
        return False

            


