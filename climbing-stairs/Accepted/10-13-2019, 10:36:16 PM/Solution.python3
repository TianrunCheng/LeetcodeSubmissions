// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        r = [0] * (n+1)
        if n == 1:
            r[1] = 1
            return r[1]
        if n == 2:
            r[2] = 2
            return r[2]
        elif n > 2:
            r[1] = 1
            r[2] = 2
            for i in range(3,n+1):
                r[i] = r[i-1] + r[i-2]

            return r[n]
                