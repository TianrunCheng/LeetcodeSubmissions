// https://leetcode.com/problems/multiply-strings

import math

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        arr_num1 = []
        for _ in num1:
            arr_num1.append(int(_))
        arr_num1.reverse()
        arr_num2 = []
        for _ in num2:
            arr_num2.append(int(_))
        arr_num2.reverse()
        
        digits = []
        res = 0
        ans = ''
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                if i+j+1 > len(digits):
                    digits.append(arr_num1[i]*arr_num2[j])
                else:
                    digits[i+j] = digits[i+j] + arr_num1[i]*arr_num2[j]
        
        i = 0
        while i < len(digits):
            ans = str(digits[i] % 10) + ans
            if digits[i] < 10:
                i = i + 1
            elif i == len(digits) - 1:
                digits.append(math.floor(digits[i]/10))
                i += 1
            else:
                digits[i+1] += math.floor(digits[i]/10)
                i += 1
        
        i = 0
        while i < len(ans)-1 and ans[i] == '0':
            i += 1
        
        return ans[i:]
                