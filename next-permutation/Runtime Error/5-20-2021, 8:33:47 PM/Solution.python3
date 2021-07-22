// https://leetcode.com/problems/next-permutation

class Solution:
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        
        right = n - 1
        left = n - 2
        
        while(left >= 0 and nums[left + 1] <= nums[left]):
            left = left - 1
        # jumps out of loop only when nums[l] < nums[l+1] or when l = 0
        
        if (left < 0):
            left = 0
            while(right > left):
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp
                right -= 1
                left += 1
            return
        
        if (left == (right-1)):
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            return
        
        # find the number just greater than nums[left] and label it sub        
        while(nums[sub] <= nums[left]):
            sub -= 1
        
        temp = nums[sub]
        nums[sub] = nums[left]
        nums[left] = temp
        
        left += 1
        while(right > left):
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            right -= 1
            left += 1
        