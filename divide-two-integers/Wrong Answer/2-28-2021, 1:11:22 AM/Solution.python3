// https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        neg = False
        if dividend < 0:
            dividend = 0 - dividend
            neg = not neg
        if divisor < 0:
            divisor = 0 - divisor
            neg = not neg
        
        powers = [divisor]  # record the 2^n * divisor values at index n
        
        while powers[-1] < dividend:
            temp = powers[-1] + powers[-1]
            powers.append(temp)
        
        bi_quotient = []
        
        for i in range(len(powers)-1, -1, -1):
            if dividend > powers[i]:
                bi_quotient.append(1)
                dividend = dividend - powers[i]
            else:
                bi_quotient.append(0)
        
        n = ''.join([str(elem) for elem in bi_quotient])
        
        if neg:
            return -int(n,2)
        
        return int(n, 2)
        