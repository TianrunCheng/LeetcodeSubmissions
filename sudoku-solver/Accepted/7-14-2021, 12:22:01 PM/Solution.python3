// https://leetcode.com/problems/sudoku-solver

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.found = False
        self.res = []
        
        def isValid(val: str, x: int, y: int) -> bool:
            # is val valid to fill in (x, y) at the time being?
            box_x = (x // 3) * 3
            box_y = (y // 3) * 3
            for i in range(3):
                for j in range(3):
                    if (box_x + i, box_y + j) != (x, y):
                        if board[box_x + i][box_y + j] == val:
                            return False
            for i in range(9):
                if i != x:
                    if board[i][y] == val:
                        return False
            for j in range(9):
                if j != y:
                    if board[x][j] == val:
                        return False
            return True
        
        def nextCell(x: int, y: int) -> (int, int):
            serial = x * 9 + y + 1
            while(serial < 81):
                i = serial // 9
                j = serial - i * 9
                if board[i][j] == ".":
                    return (i, j)
                serial += 1
            return (-1, -1)
        
        def recur(x: int, y: int):
            # try all possible digits in (x, y)
            # then fill the cells after this one
            # print((x, y))
            for i in range(1, 10):
                val = str(i)
                if isValid(val, x, y):
                    board[x][y] = val
                    next_x, next_y = nextCell(x, y)
                    if next_x < 0:
                        self.found = True
                        # print(board)
                        # self.res = board.copy()
                        # print(self.res)
                        return
                    else:
                        recur(next_x, next_y)
                        if not self.found:
                            board[x][y] = "."
            return
        
        if board[0][0] != ".":
            x, y = nextCell(0, 0)
            recur(x, y)
        else:
            recur(0, 0)
        
        # board = self.res.copy()
        return
                    
            
            