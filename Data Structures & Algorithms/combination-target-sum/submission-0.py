class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        def backtrack(i):
            if sum(sol) == target:
                res.append(sol.copy())
                return
            if sum(sol)>target or i>=len(nums):
                return
            sol.append(nums[i])
            backtrack(i)
            sol.pop()
            backtrack(i+1)
        backtrack(0)
        return res