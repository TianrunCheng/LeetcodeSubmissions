// https://leetcode.com/problems/number-of-islands


class Solution:  
    def numIslands(self, grid: List[List[str]]) -> int:
        def deleteIsland(x: int, y: int) -> bool:
            if x < 0 or x >=m or y < 0 or y >= n:
                return False
            if grid[x][y] is not "1":
                return False
            grid[x][y] = "0"
            if x > 0 and grid[x-1][y] is "1":
                deleteIsland(x-1, y)
            if x < (m-1) and grid[x+1][y] is "1":
                deleteIsland(x+1, y)
            if y > 0 and grid[x][y-1] is "1":
                deleteIsland(x, y-1)
            if y < n-1 and grid[x][y+1] is "1":
                deleteIsland(x, y+1)
            return True
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] is "1":
                    count += 1
                    deleteIsland(i, j)
        
        return count
    

                    
    
