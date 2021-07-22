// https://leetcode.com/problems/n-queens-ii

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.queens = [-1] * n
        self.count = 0
        
        def is_not_under_attack(row, col):
            for i in range(n):
                # queen in row: i, col: queens[i]
                if self.queens[i] < 0:
                    continue
                else:
                    if row == i or  col == self.queens[i]:
                        return False
                    if abs(row - i) == abs(col - self.queens[i]):
                        return False
            return True
        
        def place_queen(row, col):
            self.queens[row] = col
        
        def remove_queen(row, col):
            self.queens[row] = -1
        
        def backtrack(row = 0):
            # explore after the branches of a certain row
            # given the trace of rows before
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        self.count += 1
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)
        
        backtrack()
        return self.count
            