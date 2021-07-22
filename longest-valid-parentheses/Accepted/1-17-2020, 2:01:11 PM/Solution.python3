// https://leetcode.com/problems/longest-valid-parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # dynamic programming solution
        # store the length of the longest valid parentheses ending by the current symbol
        # if the current symbol is '(', simply put down -1, if the current symbol is ')', then:
        # dp[i] = 2 + dp[i-2](>0) if dp[i-1] == -1
        # dp[i] = 0 if dp[i-1] == 0
        # dp[i] = dp[i-1] + 2 + dp[i-2-dp[i-1]](>0) if dp[i-1]>0 and dp[i-1-dp[i-1]] == -1
        # dp[i] = 0 if dp[i-1]>0 and dp[i-1-dp[i-1]] == 0
        
        dp = [ 0 for i in range(len(s)+1)]
        max_len = 0
        
        for i in range(1, len(s)+1):
            if s[i-1] == '(':
                dp[i] = -1
            else:
                if dp[i-1] == 0:
                    dp[i] = 0
                elif dp[i-1] == -1:
                    if dp[i-2] > 0:
                        dp[i] = 2 + dp[i-2]
                        max_len = max(max_len, dp[i])
                    else:
                        dp[i] = 2
                        max_len = max(max_len, dp[i])
                elif dp[i-1] > 0:
                    if dp[i-1-dp[i-1]] == 0:
                        dp[i] = 0
                    elif dp[i-1-dp[i-1]] == -1:
                        if dp[i-2-dp[i-1]] > 0:
                            dp[i] = dp[i-1] + 2 + dp[i-2-dp[i-1]]
                            max_len = max(max_len, dp[i])
                        else:
                            dp[i] = dp[i-1] + 2
                            max_len = max(max_len, dp[i])
        
        return max_len