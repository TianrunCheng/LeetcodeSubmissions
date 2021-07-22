// https://leetcode.com/problems/set-mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # assume the nums array is in order
        # nums.sort()
        
        
        for i in range(len(nums)):
            if nums[i] != (i+1):
                return [nums[i], i+1]