// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # didn't do this problem, asked Qi for answers
        # notice 0 <= sum(nums[i]) <= 1000, meaning the possible sums induced
        #   from adding "+"/"-" before each num is within range(-1000, 1001)
        #   calculate all possibilities using dynamic programming
        
        dp = [0] * 2001
        dp[1000] = 1
        # dp_i:= [-1000, ..., 0, ..., 1000]
        # update the array "dp" 20 rounds
        # the i_th round: dp[j-1000] 
        #   meaning ways of summing up to (j-1000) using the first i nums
        
        for num in nums:
            temp_plus = [0] * 2001
            temp_minus = [0] * 2001
            for i in range(num, 2001):
                temp_plus[i] = dp[i-num]
            for i in range(0, 2001 - num):
                temp_minus[i] = dp[i+num]
            for i in range(2001):
                dp[i] = temp_plus[i] + temp_minus[i]
        
        return dp[target+1000]