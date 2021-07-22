// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.curr = []
        self.count = 0
        self.stack = []
        res = []
        
        def backtrack(ind: int):
            # print(self.curr)
            # extend ind_th symbol in current string
            if ind < 2 * n:
                if self.stack:
                    self.curr.append(')')
                    self.stack.pop()
                    backtrack(ind + 1)
                    self.curr.pop()
                    self.stack.append('(')
                if self.count < n:
                    self.curr.append('(')
                    self.stack.append('(')
                    self.count += 1
                    backtrack(ind + 1)
                    self.count -= 1
                    self.curr.pop()
                    self.stack.pop()
            else:
                res.append("".join(self.curr))
                return
        
        backtrack(0)
        
        return res