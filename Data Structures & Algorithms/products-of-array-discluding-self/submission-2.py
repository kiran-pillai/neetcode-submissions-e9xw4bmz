from functools import reduce
class Solution:
    """ Naive Solution:
    iterate through the array and compute product
    for all indices except current one
    
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final_products=[]
        for i,num in enumerate(nums):
            inter_product=1
            for j in range(len(nums)):
                if i!=j:
                    inter_product*=nums[j]
            final_products.append(inter_product)
        return final_products
        
        