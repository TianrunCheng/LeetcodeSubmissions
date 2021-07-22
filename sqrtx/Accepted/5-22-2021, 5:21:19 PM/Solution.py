// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left, right = 2, x // 2
        print(left)
        print(right)
        
        while left <= right:

            pivot = left + (right - left) // 2
            print("pivot" + str(pivot))
            num = pivot * pivot
            if num > x:
                right = pivot -1
                print("right" + str(right))
            elif num < x:
                left = pivot + 1
                print("left" + str(left))
            else:
                print("return pivot")
                return pivot
        
        print("return right")
        return right