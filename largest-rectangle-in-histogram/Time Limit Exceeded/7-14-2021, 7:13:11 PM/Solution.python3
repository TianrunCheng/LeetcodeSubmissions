// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # devide and conquer: devide from the minimum of array
        
        def helper(start: int, end: int) -> int:
            # area of the largest rectangle in [start, end + 1]
            # print(start)
            # print(end)
            # print()
            if start > end:
                # print(return 0)
                return 0
            if start == end:
                return heights[start]
            div = start
            for i in range(start, end + 1):
                if heights[i] < heights[div]:
                    div = i
            return max((end - start + 1) * heights[div], helper(start, div-1), helper(div+1, end))
        
        return helper(0, len(heights)-1)