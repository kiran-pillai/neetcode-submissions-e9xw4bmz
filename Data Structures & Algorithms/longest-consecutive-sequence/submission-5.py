class Solution:
    """
    Naive Solution:
        Make list a set
        Iterate on each num and check if next num is in set
    """
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     store=set(nums)
    #     max_counter=0
    #     for num in store:
    #         counter, curr_num= 0, num
    #         while curr_num in store:
    #             counter+=1
    #             curr_num+=1
    #         max_counter=max(max_counter,counter)
    #     return max_counter
    # """
    # Next Naive
    # Sort Array first

    # """
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     sorted_arr=sorted(list(set(nums)))
    #     max=0
    #     for i,num in enumerate(sorted_arr):
    #         is_consecutive=num==num[i-1]+1

    """
    Optimal
    Use set to check 
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums=set(nums)
        max_seq=0
        for num in set_nums:
            if num - 1 not in set_nums:
                length=1
                while length + num in set_nums:
                    length+=1
                max_seq=max(max_seq,length)
        return max_seq






