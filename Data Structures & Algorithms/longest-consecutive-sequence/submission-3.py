class Solution:
    """
    Naive Solution:
    Sort array. Check one by one what longest streak is
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        store=set(nums)
        max_counter=0
        for num in store:
            counter, curr_num= 0, num
            while curr_num in store:
                counter+=1
                curr_num+=1
            max_counter=max(max_counter,counter)
        return max_counter

