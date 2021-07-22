// https://leetcode.com/problems/third-maximum-number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
#       # this code repeats itself, could be written into a function
#         maximum = nums[0]
#         for k in nums:
#             if k > maximum:
#                 maximum = k
        
#         second = 0
#         flag = True
#         # flag: have we found at least one second-largest yet?
#         # flag = True : value of second un-set
#         for k in nums:
#             if k != maximum:
#                 if flag:
#                     second = k
#                     flag = False
#                 else:
#                     second = max(second, k)
        
#         if flag:
#             return maximum
        
#         third = 0
#         flag = True
#         # flag is True when the value of "third" is unset
#         for k in nums:
#             if k != maximum and k != second:
#                 if flag:
#                     third = k
#                     flag = False
#                 else:
#                     third = max(third, k)
#         if flag:
#             return maximum
        
#         return third

        def findMaximumIgnoreNums(nums, seenMaximums):
            maximum = None
            for k in nums:
                if k not in seenMaximums:
                    if maximum == None or maximum < k:
                        maximum = k
            return maximum
        
        seen = set()
        
        for _ in range(3):
            current_maximum = findMaximumIgnoreNums(nums, seen)
            if current_maximum == None:
                return max(seen)
            seen.add(current_maximum)
        
        return min(seen)
        