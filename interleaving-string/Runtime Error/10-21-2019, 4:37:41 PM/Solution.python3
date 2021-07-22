// https://leetcode.com/problems/interleaving-string

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if len(s3) != (m+n):
            return False
        else:
            inter = [0] * (m+1)
            for i in range(m+1):
                inter[i] = [0] * (n+1)
            for i in range(m+1):
                inter[0][i] = 1
            for i in range(n+1):
                inter[i][0] = 1

            for i in range(1, n+1):
                for j in range(1, m+1):
                    if inter[i-1][j] == 1 and s3[i+j-1] == s1[i-1]:
                        inter[i][j] = 1
                    elif inter[i][j-1] == 1 and s3[i+j-1] == s2[j-1]:
                        inter[i][j] = 1
            if inter[m][n] == 0:
                return False
            else:
                return True