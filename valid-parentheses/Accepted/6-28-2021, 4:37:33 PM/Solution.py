// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c is "(":
                stack.append(c)
            elif c is "[":
                stack.append(c)
            elif c is "{":
                stack.append(c)
            elif c is ")":
                if len(stack) > 0:
                    if stack.pop() is "(":
                        pass
                    else:
                        return False
                else:
                    return False
            elif c is "]":
                if len(stack) > 0:
                    if stack.pop() is "[":
                        pass
                    else:
                        return False
                else:
                    return False
            elif c is "}":
                if len(stack) > 0:
                    if stack.pop() is "{":
                        pass
                    else:
                        return False
                else:
                    return False
        
        if len(stack) is 0:
            return True