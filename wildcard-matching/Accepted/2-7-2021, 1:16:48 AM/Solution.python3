// https://leetcode.com/problems/wildcard-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        
        match = [ False  ]* (n+1)
        match[0] = True
        
        for j in range(m):
            if p[j] is "*":
                for i in range(n):
                    if match[i]:
                        match[i+1] = True
                # print(match)
            elif p[j] is "?":
                trans = [ False ] * (n+1)
                for i in range(n):
                    if match[i]:
                        trans[i+1] = True
                match = trans
                # print(match)
            else:
                trans = [ False  ]* (n+1)
                for i in range(n):
                    if match[i] and s[i] == p[j]:
                        trans[i+1] = True
                match = trans
                # print(match)
        
        return match[-1]
                        