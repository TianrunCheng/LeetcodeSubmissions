// https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        summation = n * (n + 1) // 2
        
        for num in nums:
            summation -= num
        
        return summation