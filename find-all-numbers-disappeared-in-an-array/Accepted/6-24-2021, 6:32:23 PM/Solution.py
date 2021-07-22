// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            curr = abs(nums[i])
            if nums[curr-1] > 0:
                nums[curr-1] *= -1
        
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        
        return res