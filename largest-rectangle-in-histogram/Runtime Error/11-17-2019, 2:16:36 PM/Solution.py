// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = max(heights)
        for i in range(1, n):
            for j in range(n-i):
                heights[j] = min(heights[j], heights[j+1])
                max_area = max(heights[j] * (i+1), max_area)
        return max_area