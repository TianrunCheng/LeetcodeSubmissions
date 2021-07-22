// https://leetcode.com/problems/minimum-path-sum

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)   # number of rows
        n = len(grid[0])    # number of columns
        
        res = [0] * n
        
        
        for i in range(m):
            if i == 0:
                for j in range(n):
                    if j == 0:
                        res[j] = grid[i][j]
                    else:
                        res[j] = res[j-1] + grid[i][j]
            else:
                for j in range(n):
                    if j == 0:
                        res[j] = res[j] + grid[i][j]
                    else:
                        swap = min(res[j-1], res[j])
                        res[j] = grid[i][j] + swap
        return res[-1]
            