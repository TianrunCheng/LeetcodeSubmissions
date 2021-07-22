// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # n = len(heights)
        # if n == 0:
        #     return 0
        # max_area = max(heights)
        # for i in range(1, n):
        #     for j in range(n-i):
        #         heights[j] = min(heights[j], heights[j+1])
        #         max_area = max(heights[j] * (i+1), max_area)
        # return max_area
        
        # n = len(heights)
        # if n == 0:
        #     return 0
        # max_area = 0
        # for i in range(n):
        #     w = 0
        #     j = i
        #     while j < n and heights[j] >= heights[i]:
        #         w += 1
        #         j += 1
        #     j = i - 1
        #     while j >= 0 and heights[j] >= heights[i]:
        #         w += 1
        #         j = j-1
        #     if max_area < heights[i] * w:
        #         max_area = heights[i] * w
        # return max_area
        
        n = len(heights)
        if n == 0:
            return 0
        
        heights.append(0)
        stack = [-1]
        maxarea = 0
        for i in range(n):
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                curr = heights[i]
                while heights[stack[-1]] > curr:
                    h = heights[stack.pop(-1)]
                    w = i - stack[-1] - 1
                    maxarea = max(maxarea, h * w)
                stack.append(i)
        while stack[-1] != -1:
            h = heights[stack.pop(-1)]
            w = n - stack[-1] - 1
            maxarea = max(maxarea, h * w)
        
        return maxarea
        
    