// https://leetcode.com/problems/regular-expression-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        rows = 1 + len(s)
        cols = 1 + len(p)
        arr = [[False for i in range(cols)] for j in range(rows)]
        arr[0][0] = True

        i = 1
        while i < cols:
            if i < cols-1 and p[i] == '*':
                i = i + 1
                for j in range(rows):
                    if arr[j][i-2]:
                        arr[j][i] = True
                    elif j > 0 and arr[j-1][i] and (p[i-2] == '.' or p[i-2] == s[j-1]):
                        arr[j][i] = True
                i = i + 1
            else:
                for j in range(rows):
                    if j > 0 and arr[j-1][i-1] and (p[i-1] == '.' or p[i-1] == s[j-1]):
                        arr[j][i] = True
                i = i + 1
        
        return arr[rows-1][cols-1]