// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # iterative, as traversing the array:
        # use stack to remember each height's earliest start point
        # when pop stack, calculate all max rectangles ending in current index
        # heights.append(0)
        # add a sentinel, so that after the last height, we will do a round of pop
        stack = [(heights[0], 0)]
        # (current_heights_not_ending, earliest_start_ind)
        large = 0
        curr_ind = 1
        while curr_ind < len(heights):
            print(stack)
            curr_h = heights[curr_ind]
            if curr_h > stack[-1][0]:
                stack.append((curr_h, curr_ind))
                curr_ind += 1
            if curr_h == stack[-1][0]:
                curr_ind += 1
            else:
                # curr_h < stack[-1][0], start calculating
                while stack and stack[-1][0] > curr_h:
                    early_h, early_ind = stack.pop()
                    area = early_h * (curr_ind - early_ind)
                    if large < area:
                        large = area
                if not stack:
                    # curr is the min so far
                    stack.append((curr_h, 0))
                if stack[-1][0] < curr_h:
                    stack.append((curr_h, early_ind))
                curr_ind += 1
            
        curr_h, curr_ind = 0, len(heights)
        while stack and stack[-1][0] > curr_h:
            early_h, early_ind = stack.pop()
            area = early_h * (curr_ind - early_ind)
            if large < area:
                large = area
        
        return large
        
        # # worst case O(n ^ 2)
#         # devide and conquer: devide from the minimum of array

#         def helper(start: int, end: int) -> int:
#             # area of the largest rectangle in [start, end + 1]
#             if start > end:
#                 return 0
#             if start == end:
#                 return heights[start]
#             div = (end - start) // 2 + start
#             for i in range(start, end + 1):
#                 if heights[i] < heights[div]:
#                     div = i
#             return max((end - start + 1) * heights[div], helper(start, div-1), helper(div+1, end))
        
#         return helper(0, len(heights)-1)