// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = j = 0
        # i: read pointer
        # j: write pointer
        
        for i in range(n):
            if nums[i] == 0:
                i += 1
            else:
                nums[j] = nums[i]
                j += 1
        
        while(j < n):
            nums[j] = 0
            j += 1
        
        return