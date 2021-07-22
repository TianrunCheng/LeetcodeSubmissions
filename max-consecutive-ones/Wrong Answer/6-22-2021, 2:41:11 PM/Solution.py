// https://leetcode.com/problems/max-consecutive-ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        flag = False
        
        
        for k in nums:
            if flag:
                if k == 1:
                    curr += 1
                else:
                    flag = False
                    if curr > res:
                        res = curr
                    curr = 0
            else:
                if k == 1:
                    flag = True
                    curr += 1
        
        return res
        
        
        