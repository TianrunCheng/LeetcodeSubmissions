// https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n < 2:
            return
        
        for i in range(n//2):
            for j in range(i, n-i-1):
                # print(i, j)
                mem = matrix[i][j]
                
                swap = matrix[j][n-1-i]
                matrix[j][n-1-i] = mem
                mem = swap
                
                swap = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = mem
                mem = swap
                
                swap = matrix[n-j-1][i]
                matrix[n-j-1][i] = mem
                mem = swap
                
                matrix[i][j] = mem
                # print(matrix)
                