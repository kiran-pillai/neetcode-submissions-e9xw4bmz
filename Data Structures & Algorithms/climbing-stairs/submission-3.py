class Solution:
    def __init__(self):
        self.cache = {}
    def countPaths(self, n):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.countPaths(n-1) + self.countPaths(n-2)
        return self.cache[n]
    def climbStairs(self, n: int) -> int:
        return self.countPaths(n)
       
        
        