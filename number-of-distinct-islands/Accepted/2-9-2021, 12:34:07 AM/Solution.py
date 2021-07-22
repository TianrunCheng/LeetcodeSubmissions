// https://leetcode.com/problems/number-of-distinct-islands

class Solution:
    
    global curr_shape, m, n
    global shape
    
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        def deleteIsland(x: int, y: int, size: int, curr_shape: [str]):
            if x < 0 or x >=m or y < 0 or y >= n:
                return ""
            if grid[x][y] is not 1:
                return ""

            grid[x][y] = 0
            if y < n-1 and grid[x][y+1] is 1:  # going right
                curr_shape.append("r" + str(size))
                # print(curr_shape)
                # print(grid)
                deleteIsland(x, y+1, size+1, curr_shape)
            if x < (m-1) and grid[x+1][y] is 1:  # going down
                curr_shape.append("d" + str(size))
                # print(curr_shape)
                # print(grid)
                deleteIsland(x+1, y, size+1, curr_shape)
            if x > 0 and grid[x-1][y] is 1: # going up
                curr_shape.append("u" + str(size))
                # print(curr_shape)
                # print(grid)
                deleteIsland(x-1, y, size+1, curr_shape)
            if y > 0 and grid[x][y-1] is 1:  # going left
                curr_shape.append("l" + str(size))
                # print(curr_shape)
                # print(grid)
                deleteIsland(x, y-1, size+1, curr_shape)
            return curr_shape
    
        m = len(grid)
        n = len(grid[0])
        shape = {}
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] is 1:
                    curr_shape = []
                    curr_shape = deleteIsland(i, j, 0, curr_shape)
                    curr_shape_str = ''.join([str(elem) for elem in curr_shape])
                    # print(curr_shape_str)
                    if curr_shape_str not in shape:
                        shape[curr_shape_str] = 0
        
        return len(shape)
