// https://leetcode.com/problems/sort-array-by-parity

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        # i: all elements to the left of i are even
        j = n-1
        # j: all elements to the right of j are odd
        
        while(i < j):
            while(nums[i] % 2 == 0 and i < n): 
                i += 1
            while(nums[j] % 2 == 1 and j >= 0):
                j -= 1
            if i < j:
                swap = nums[i]
                nums[i] = nums[j]
                nums[j] = swap
                i += 1
                j -= 1
        
        return nums