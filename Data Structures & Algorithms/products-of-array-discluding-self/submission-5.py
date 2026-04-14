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
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def get_product(lis):
            return reduce(lambda x,y : x*y, lis)
        product=get_product(nums)
        final_products=[]
        for num in nums:
            if num!=0:
                final_products.append(product//num)
            else:
                countZeroes=list(filter(lambda x: x==0, nums))
                nonZeroes=list(filter(lambda x: x!=0, nums))
                print(countZeroes)
                if len(countZeroes)==1:
                    final_products.append(get_product(nonZeroes))
                elif len(countZeroes)>1:
                    final_products.append(0)
             

                
        return final_products
          

    """
    Non-Naive Solution:
    Prefix and Suffix 
    """
        
        