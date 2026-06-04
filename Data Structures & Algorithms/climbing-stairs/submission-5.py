"""

"""

class Solution:
    def __init__(self):
        self.cache = {}
    def climbStairs(self, n: int) -> int:
        if n<1:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in self.cache:
            return self.cache[n]
        else:
            self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.cache[n]
