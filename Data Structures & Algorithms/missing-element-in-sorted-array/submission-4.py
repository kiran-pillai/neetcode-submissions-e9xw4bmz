class Solution:
    """
    Find missing numbers with current bounds
        - if k>len(missing_nums)
        - use a while loop to increment by one till k is hit 
    """
    def missingElement(self, nums: List[int], k: int) -> int:
        missing_nums = []
        if len(nums)>1:
            for i in range(len(nums)):
                if i == 0:
                    continue
                diff = nums[i] - nums[i-1]
                if diff>1:
                    for missing_num in range(nums[i-1]+1, nums[i]):
                        missing_nums.append(missing_num)
                        if len(missing_nums) == k:
                            return missing_nums[-1]

        last_val = nums[-1]
        # remaining k values
        needed = k - len(missing_nums)
        return last_val + needed