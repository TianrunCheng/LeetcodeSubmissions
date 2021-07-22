// https://leetcode.com/problems/01-matrix

from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        bfs = deque()
        
        m = len(mat)
        n = len(mat[0])
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    bfs.append((i, j))
                else:
                    mat[i][j] = float("inf")
        
        step = 0
        while(len(bfs) > 0):
            size = len(bfs)
            step += 1
            for _ in range(size):
                cur = bfs.popleft()
                if cur[0] > 0 and mat[cur[0] - 1][cur[1]] > step:
                    mat[cur[0] - 1][cur[1]] = step
                    bfs.append((cur[0]-1, cur[1]))
                if cur[0] < (m - 1) and mat[cur[0] + 1][cur[1]] > step:
                    mat[cur[0] + 1][cur[1]] = step
                    bfs.append((cur[0]+1, cur[1]))
                if cur[1] > 0 and mat[cur[0]][cur[1] - 1] > step:
                    mat[cur[0]][cur[1] - 1] = step
                    bfs.append((cur[0], cur[1]-1))
                if cur[1] < (n - 1) and mat[cur[0]][cur[1] + 1] > step:
                    mat[cur[0]][cur[1] + 1] = step
                    bfs.append((cur[0], cur[1]+1))
        return mat
        
        