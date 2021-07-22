// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if s == '' or len(set(list(s))) == 1:
            return s
        
        
        matrix = [[False]* len(s) for _ in range(len(s))]
        for i in range(len(s)):
            matrix[i][i] = True
        ms = s[0]
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                matrix[i][i+1] = True
                ms = s[i:i+2]
                
        # print(matrix)
        for i in range(3, len(s)+1):  # len of palindrome checking currently 
            for j in range(len(s) - i +1):
                if s[j] == s[j+i-1] and matrix[j+1][j+i-2] == True:
                    matrix[j][j+i-1] = True
                    ms = s[j:j+i]
                    # print(ms)
                else:
                    matrix[j][j+i-1] = 0
       
        return ms
        