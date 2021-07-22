// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # DFS: recursion with memoization
        # is it true that all dynamic programming can be 
        #   implemented via recursion with memoization?
        
        mem = []
        for i in range(len(nums)):
            mem.append([float("inf")] * 2001)
        for i in range(2001):
            mem[0][i] = 0
        mem[0][nums[0] + 1000] += 1
        mem[0][-nums[0] + 1000] += 1
        # mem[i][s+1000]: ways of nums[0:i+1] summing to s
        
        def rec(i: int, s: int) -> int:
            # recursive func
            # rec(i, s) = mem[i][s]
            nonlocal mem
            # print("recur")
            # print(i)
            # print(s)
            if s < -1000 or s > 1000:
                # print("return 0")
                return 0
            if i == 0:
                # print("return " + str(mem[0][s+1000]))
                return mem[0][s+1000]
            if mem[i][s+1000] != float("inf"):
                # print("return " + str(mem[i][s+1000]))
                return mem[i][s+1000]
            mem[i][s+1000] = rec(i-1, s - nums[i]) + rec(i-1, s + nums[i])
            # print("return " + str(mem[i][s+1000]))
            # nums[0: i-1] sum to "s +- nums[i]"
            return mem[i][s+1000]
        
        return rec(len(nums)-1, target)
        
        
#         # didn't do this problem, asked Qi for answers
#         # notice 0 <= sum(nums[i]) <= 1000, meaning the possible sums induced
#         #   from adding "+"/"-" before each num is within range(-1000, 1001)
#         #   calculate all possibilities using dynamic programming
        
#         dp = [0] * 2001
#         dp[1000] = 1
#         # dp_i:= [-1000, ..., 0, ..., 1000]
#         # update the array "dp" 20 rounds
#         # the i_th round: dp[j-1000] 
#         #   meaning ways of summing up to (j-1000) using the first i nums
        
#         for num in nums:
#             temp_plus = [0] * 2001
#             temp_minus = [0] * 2001
#             for i in range(num, 2001):
#                 temp_plus[i] = dp[i-num]
#             for i in range(0, 2001 - num):
#                 temp_minus[i] = dp[i+num]
#             for i in range(2001):
#                 dp[i] = temp_plus[i] + temp_minus[i]
        
#         return dp[target+1000]
    