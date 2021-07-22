// https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        nums = [1 for i in range(n)]
        
        for j in range(m-1):
            for i in range(1, n):
                nums[i] = nums[i-1] + nums[i]
        
        return nums[-1]