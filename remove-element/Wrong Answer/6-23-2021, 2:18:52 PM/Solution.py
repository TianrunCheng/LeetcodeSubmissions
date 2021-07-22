// https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        j = n-1
        # i: the next to examine, left of i are all set
        # j: the current last element of the list
        
        while(i < j):
            if nums[i] != val:
                i += 1
            else:
                while(nums[j] == val):
                    j -= 1
                if j > i:
                    nums[i] = nums[j]
                    j -= 1
        
        return j + 1
                
                