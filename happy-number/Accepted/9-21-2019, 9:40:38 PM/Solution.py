// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        
        def happy_iter(i: int) -> int:
            j = 0
            while(i>=10):
                    j += (i%10)**2
                    i = (i-i%10)/10
                
            j += i**2
            return j
          
        
        while (n>10):
            n = happy_iter(n)
        
        if (n==10 or n==1 or n==7):
            return True
        else:
            return False
                
        