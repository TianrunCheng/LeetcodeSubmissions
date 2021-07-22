// https://leetcode.com/problems/climbing-stairs

class Solution:
    
    def __init__(self):
        self.cache = {}
    
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        if n in self.cache:
            return self.cache[n]
        res = self.climbStairs[n-1] + self.climbStairs[n-2]
        self.cache[n] = res
        return res
        