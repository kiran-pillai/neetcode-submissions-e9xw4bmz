class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=[]
        for num in nums:
            print(num in seen, num, seen)
            if num in seen:
                print(num)
                return True
            seen.append(num)
        return False
        