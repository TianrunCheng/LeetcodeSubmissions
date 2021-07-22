// https://leetcode.com/problems/evaluate-reverse-polish-notation

import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # use a stack to store not used operands
        # when meeting a operate, pop out two most recent operands
        # straight forward from the definition of RPN
        
        stack = []
        
        for i in range(len(tokens)):
            curr = tokens[i]
            if curr == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif curr == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif curr == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif curr == "/":
                b = stack.pop()
                a = stack.pop()
                f = a / b
                if f > 0:
                    stack.append(math.floor(f))
                else:
                    stack.append( - math.floor(-f))
            else:
                stack.append(int(curr))
        
        return stack[-1]