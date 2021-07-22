// https://leetcode.com/problems/max-consecutive-ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         res = 0
#         curr = 0
#         flag = False
#         # starting we were not in a "1" session
        
#         for k in nums:
#             if flag:
#                 # we were in a "1" session
#                 if k == 1:
#                     curr += 1
#                     # we change res each time we change curr
#                     if curr > res:
#                         res = curr
#                 else:
#                     flag = False
#                     curr = 0
#             else:
#                 if k == 1:
#                     flag = True
#                     curr += 1
#                     if curr > res:
#                         res = curr
        
#         return res
        
        count = max_count = 0
        
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 0
        
        return max(max_count, count)
        