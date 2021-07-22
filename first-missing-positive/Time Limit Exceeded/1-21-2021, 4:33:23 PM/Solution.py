// https://leetcode.com/problems/first-missing-positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 0
            elif nums[i] == i+1:
                pass
            else:
                j = i  # j = current element's index
                x = nums[i]  # x = current element's value
                if nums[x-1] < 1 or nums[x-1] > n or nums[x-1] == x:
                    nums[x-1] = x
                    nums[j] = 0
                else:
                    spam = nums[x-1]
                    nums[j] = 0
                    j = spam - 1
                    x = nums[j]
                    while(nums[x-1] >= 1 and nums[x-1] <= n and nums[x-1] != x):
                        spam = nums[x-1]
                        nums[j] = 0
                        j = spam - 1
                        x = nums[j]
                    nums[x-1] = x
                    nums[j] = 0
        
        for i in range(n):
            if nums[i] != i+1:
                return (i+1)