from functools import reduce
class Solution:
    """ Naive Solution:
    iterate through the array and compute product
    for all indices except current one
    
    """
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     final_products=[]
    #     for i,num in enumerate(nums):
    #         inter_product=1
    #         for j in range(len(nums)):
    #             if i!=j:
    #                 inter_product*=nums[j]
    #         final_products.append(inter_product)
    #     return final_products


    """
    Division:
    Get the product of the whole array. 
    Use division on non-zero numbers to get answer
    """
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     def get_product(lis):
    #         return reduce(lambda x,y : x*y, lis)
    #     product=get_product(nums)
    #     final_products=[]
    #     countZeroes=list(filter(lambda x: x==0, nums))
    #     nonZeroes=list(filter(lambda x: x!=0, nums))
    #     for num in nums:
    #         if num!=0:
    #             final_products.append(product//num)
    #         else:
    #             print(countZeroes)
    #             if len(countZeroes)==1:
    #                 final_products.append(get_product(nonZeroes))
    #             elif len(countZeroes)>1:
    #                 final_products.append(0)
             

                
    #     return final_products
    """
    Division (cleaned up):
    Get the product of the whole array. 
    Use division on non-zero numbers to get answer
    """
    # def productExceptSelf(self, nums:List[int]) -> List[int]:
    #     def get_product(lis):
    #         return reduce(lambda x,y : x*y, lis)
    #     totalZeroes=list(filter(lambda x: x==0, nums))
    #     nonZeroes=list(filter(lambda x: x!=0, nums))
    #     if len(totalZeroes)>1:
    #         return [0]*len(nums)

    #     elif len(totalZeroes)==1:
    #         return [get_product(nonZeroes) if num==0 else 0 for num in nums]

    #     product=get_product(nums)
    #     return list(map(lambda x: product//x, nums))


    """
    Non-Naive Solution:
    Prefix and Suffix 
    Input: nums = [1,2,4,6] 
    prefix array: [1,2,8,48]
    suffix array: [48,48,24,6]
    ex: index 1 (2)
    left -1 = prefix[n-1] = 1
    right + len(array -right) = 24

    get index of prefix (n-1)
    get index of suffix len(arr)-n
    """

    def productExceptSelf(self, nums:List[int]) -> List[int]:
        prefix_arr=[]
        prefix=1
        for num in nums:
            next_step=prefix*num
            prefix=next_step
            prefix_arr.append(next_step)

        postfix_arr=[]
        postfix=1
        for num in reversed(nums):
            next_step=postfix*num
            postfix=next_step
            postfix_arr.insert(0,next_step)

        final_array=[]
        for i in range(len(nums)):
            prefix=prefix_arr[i-1] if i-1>=0 else 1
            postfix=postfix_arr[i+1] if i+1!=len(nums) else 1
            final_array.append(prefix*postfix)
        
        return final_array


           
        

    

    
        
        