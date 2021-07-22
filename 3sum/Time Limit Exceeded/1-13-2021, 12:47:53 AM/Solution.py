// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # len(nums) <= 3000, somehow allows n^2 complexity
        # nums[i] would not exceed python int arrange: 4 bytes -> 2^32 -> 10^9
        
        result = []
        if len(nums) < 3:
            return result
        
        nums.sort()
        # print(nums)
        def binary_search(lookup: List[int], key) -> bool:
            # print(lookup)
            # print(key)
            lo = 0
            hi = len(lookup) - 1
            while(lo <= hi):
                mid = lo + (hi - lo) // 2
                if key < lookup[mid]:
                    hi = mid - 1
                elif key > lookup[mid]:
                    lo = mid + 1
                else:
                    return True
            return False
        
        
        for i in  range(len(nums)-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            curr_result = []
            for j in range(i+1, len(nums)-1):
                if j > (i+1) and nums[j]==nums[j-1]:
                    continue
                curr_sum = nums[i] + nums[j]
                if binary_search(nums[j+1:], -curr_sum):
                    curr_result = [nums[i], nums[j], -curr_sum]
                    result.append(curr_result)
        
        return result
                