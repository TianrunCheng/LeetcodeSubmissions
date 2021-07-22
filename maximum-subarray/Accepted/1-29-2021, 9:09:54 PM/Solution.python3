// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_low = 0
        curr_sum = 0
        result = nums[0]
        
        for x in nums:
            curr_sum += x
            this_max = curr_sum - curr_low
            if curr_sum < curr_low:
                curr_low = curr_sum
            if this_max > result:
                result = this_max
        
        return result