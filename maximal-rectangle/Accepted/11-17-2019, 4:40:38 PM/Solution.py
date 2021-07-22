// https://leetcode.com/problems/maximal-rectangle

class Solution:
    
    def leetcode84(self, heights):
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
    
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        if not matrix:
            return 0
        
        maxarea = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[j] += 1
                else:
                    dp[j] = 0
            
            maxarea = max(maxarea, self.leetcode84(dp))
        
        return maxarea
    