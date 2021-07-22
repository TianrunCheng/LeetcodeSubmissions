// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        # i: length of resulting array at the time being
        #   - also the index of the next index free for inserting values
        for j in range(n):
            if i == 0:
                i += 1
            elif nums[i-1] != nums[j]:
                nums[i] = nums[j]
                i += 1
            
        return i