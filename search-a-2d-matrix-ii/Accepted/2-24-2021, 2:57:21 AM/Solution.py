// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def searchRectangle(left, up, right, down):
            
            if left > right or up > down:
                return False
            
            if matrix[up][left] > target or matrix[down][right] < target:
                return False
            
            mid = left + (right - left) // 2
            row = up
            
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            # matrix[row][mid] > target, matrix[row-1][mid] < target
            
            return searchRectangle(left, row, mid-1, down) or searchRectangle(mid+1, up, right, row-1)
        
        
        return searchRectangle(0, 0, len(matrix[0])-1, len(matrix)-1)