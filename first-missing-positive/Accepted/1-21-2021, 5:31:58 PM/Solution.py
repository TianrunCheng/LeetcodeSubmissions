// https://leetcode.com/problems/first-missing-positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            j = nums[i] - 1
            # put num[i] to the correct place if nums[i] in the range [1, n]
            if 0 <= j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        # so far, all the integers that could find their own correct place 
        # have been put to the correct place, next thing is to find out the
        # place that occupied wrongly
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
#         n = len(nums)
#         if n == 0:
#             return 1
        
#         for i in range(n):
#             # ii = i  # the starting index
#             # x = nums[ii]  # the value on starting index
#             # print("i is " + str(i))
#             if nums[i] < 1 or nums[i] > n:
#                 nums[i] = 0  # omit this number
#                 # print(nums)
#             elif nums[i] == i+1:
#                 pass  # leave the already found pos int be
#             else:  # need to find index x-1 and mark its been found
                
                
#                 x = nums[i]  # the value to be recorded
#                 swap = nums[x-1]  # remember the number originally occupying the [x-1] index
#                 nums[x-1] = x  # record that x has been found
#                 nums[i] = 0
#                 # print(nums)
#                 # print(swap)
#                 # ii = x - 1  # new starting index
#                 x =  swap   # new value to record
#                 while(x >=1 and x<=n and nums[x-1] != x):
                    
#                     swap = nums[x-1]
#                     nums[x-1] = x
#                     x = swap
#                     print(nums)
#                     print(swap)
                          
#         print(nums)
#         for i in range(n):
#             if nums[i] != i+1:
#                 return (i+1)
        
#         return n+1