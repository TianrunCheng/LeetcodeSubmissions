// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        r = []
        for i in range(n):
            r.append([0]*n)
        if n == 1:
            return s
        if n == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        else:
            for i in range(n):
                r[i][i] = 1
            a = s[i]
            for i in range(n-1):
                if s[i] == s[i+1]:
                    r[i][i+1] = 2
                    a = s[i-1:i+1]
                else:
                    r[i][i+1] = 1
            for l in range(3, n+1):
                for i in range(n-l+1):
                    if s[i] == s[i+l-1] and r[i+1] [i+l-2] == l-2:
                        r[i][i+l-1] = l
                        a = s[i-1:i+l-1]
                    else:
                        r[i] [i+l-1] = max(r[i][i+l-2], r[i+1][i+l-1])
            return a
                
            