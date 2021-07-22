// https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        curr_max = 0
        curr_height = 0
        last_height = 0
        if n < 2:
            return 0
        
        left = 0
        right = n-1
        
        while right > left:
            curr_height = min(height[left], height[right])
            if curr_height > last_height:
                rectangle = (right - left) * curr_height
                curr_max = max(curr_max, rectangle)
                last_height = curr_height
            if height[right] >= height[left]:
                left += 1
            else:
                right -= 1
        
        return curr_max
        
    
#         # Brute Force: O(n^2) worst case
#         # Note: n -> 3 * 10^4, too large
        
#         curr_max = 0
#         if len(height) < 2:
#             return 0
        
#         for i in range(len(height)-1):
#             if height[i] is 0:
#                 continue
#             if i>0 and height[i] <= height[i-1]:
#                 continue
#             if (curr_max / height[i]) > (len(height)-1-i):
#                 continue
#             else:
#                 for k in range(len(height)-i):
#                     j = len(height)-k-1
#                     container = (j - i) * min(height[i], height[j])
#                     # print(container)
#                     if curr_max > container:
#                         pass
#                     else:
#                         curr_max = container
                        
#                     if height[j] >= height[i]:
#                         break
        
#         return curr_max



