// https://leetcode.com/problems/first-missing-positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 1
        
        for i in range(n):
            # ii = i  # the starting index
            # x = nums[ii]  # the value on starting index
            # print("i is " + str(i))
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 0  # omit this number
                # print(nums)
            elif nums[i] == i+1:
                pass  # leave the already found pos int be
            else:  # need to find index x-1 and mark its been found
                
                
                x = nums[i]  # the value to be recorded
                swap = nums[x-1]  # remember the number originally occupying the [x-1] index
                nums[x-1] = x  # record that x has been found
                nums[i] = 0
                # print(nums)
                # print(swap)
                # ii = x - 1  # new starting index
                x =  swap   # new value to record
                while(x >=1 and x<=n and nums[x-1] != x):
                    
                    swap = nums[x-1]
                    nums[x-1] = x
                    x = swap
                    print(nums)
                    print(swap)
                    
                # nums[x-1] = x
                # print(nums)
        
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                # print(j, x)
                # print(nums)
                # if nums[x-1] < 1 or nums[x-1] > n or nums[x-1] == x:
                #     nums[x-1] = x
                #     nums[j] = 0
                #     print(j, x)
                #     print(nums)
                # else:
                #     spam = nums[x-1]
                #     nums[x-1] = x
                #     nums[j] = 0
                #     j = spam - 1
                #     if nums[j] < 1 or nums[j] > n or nums[j] == j+1:
                #         nums[j] = j+1
                #     else:
                #         x = nums[j]
                #         print(j, x)
                #         print(nums)
                #         while(nums[x-1] >= 1 and nums[x-1] <= n and nums[x-1] != x):
                #             spam = nums[x-1]
                #             nums[j] = 0
                #             j = spam - 1
                #             if nums[j] < 1 or nums[j] > n or nums[j] == j+1:
                #                 nums[j] = j+1
                #                 break
                #             else:
                #                 x = nums[j]
                #                 print(j, x)
                #                 print(nums)
                #         nums[x-1] = x
                #         nums[j] = 0
                #         print(j, x)
                #         print(nums)
        
        print(nums)
        for i in range(n):
            if nums[i] != i+1:
                return (i+1)
        
        return n+1