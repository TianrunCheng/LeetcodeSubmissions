// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = 1024 * 64
        # r * r = 2^16 * 2^16 = 2^32 (largest_int)
        
        if x < r:
            r = x
        
        while ( l <= r ):
            m = (l + r) // 2
            if (m+1) * (m+1) < x:
                l = m+1
            elif x < (m+1) * (m+1):
                if m * m <= x:
                    return m
                else:
                    r = m-1
            else:
                return m+1

#  result <= target < result+1
#
#                         x
#                         | 
# [0, ..., pivot-1, pivot, pivot+1, ... , m]
#  l                  m                    r
#     