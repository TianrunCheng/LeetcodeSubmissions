// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def fn(n: int) -> List[str]:
            ans = []
            if n == 1:
                return ["()"]
            else:
                for i in range(n):
                    if i > 0 and n-1-i > 0:
                        sub_ans2 = fn(i)
                        sub_ans1 = fn(n-1-i)
                        for a in sub_ans1:
                            for b in sub_ans2:
                                ans.append('('+a+')'+b)
                    elif i == 0:
                        sub_ans = fn(n-1)
                        for _ in sub_ans:
                            ans.append('('+_+')')
                    elif i == n-1:
                        sub_ans = fn(n-1)
                        for _ in sub_ans:
                            ans.append('()'+_)
                return ans
                    
        if n == 0:
            return []
        else:
            return fn(n)