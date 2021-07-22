// https://leetcode.com/problems/maximal-rectangle

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        line = []
        for i in range(len(matrix)):
            line.append([])
            for j in range(len(matrix[0])):
                line[i].append(0)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                k = j
                while k < len(matrix[0]) and matrix[i][k] == '1':
                    line[i][j] += 1
                    k += 1

        max_rec = 0
        curr_lis = []
        for j in range(len(line[0])):
            for i in range(len(line)):
                curr_lis.append(line[i][j])
                max_rec = max(line[i][j], max_rec)
            for k in range(1, len(line[0])):
                for _ in range(len(curr_lis)-1):
                    curr_lis[_] = min(curr_lis[_], curr_lis[_+1])
                    max_rec = max(curr_lis[_] * (k+1), max_rec)
                curr_lis.pop(-1)
        
        return max_rec
