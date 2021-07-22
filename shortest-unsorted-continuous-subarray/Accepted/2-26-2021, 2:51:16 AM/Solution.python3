// https://leetcode.com/problems/shortest-unsorted-continuous-subarray

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        helper = []
        for n in nums:
            helper.append(n)
        
        helper.sort()
        # print(helper)
        start = 0
        end = 0
        for i in range(len(nums)):
            if nums[i] != helper[i]:
                start = i
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i] != helper[i]:
                end = i
                break
        
        if end == start:
            return 0
        
        return (end - start + 1) 