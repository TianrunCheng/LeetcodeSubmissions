// https://leetcode.com/problems/third-maximum-number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maximum = nums[0]
        for k in nums:
            if k > maximum:
                maximum = k
        
        second = 0
        flag = True
        # flag: have we found at least one second-largest yet?
        # flag = True : value of second un-set
        for k in nums:
            if k != maximum:
                if flag:
                    second = k
                    flag = False
                else:
                    second = max(second, k)
        
        if flag:
            return maximum
        
        third = 0
        flag = True
        # flag is True when the value of "third" is unset
        for k in nums:
            if k != maximum and k != second:
                if flag:
                    third = k
                    flag = False
                else:
                    third = max(third, k)
        if flag:
            return maximum
        
        return third
        