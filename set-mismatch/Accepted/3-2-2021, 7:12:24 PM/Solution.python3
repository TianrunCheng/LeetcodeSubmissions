// https://leetcode.com/problems/set-mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic = {}
        n = len(nums)
        dup = 0
        mis = 0
        
        for num in nums:
            if num not in dic:
                dic[num] = 0
            else:
                dup = num
        
        for i in range(1, n+1, 1):
            if i not in dic:
                mis = i
        
        return [dup, mis]

        