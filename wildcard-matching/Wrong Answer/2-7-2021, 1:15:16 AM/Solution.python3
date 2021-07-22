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
                        match[i+1]
            elif p[j] is "?":
                trans = [ False ] * (n+1)
                for i in range(n):
                    if match[i]:
                        trans[i+1] = True
                match = trans
            else:
                trans = [ False  ]* (n+1)
                for i in range(n):
                    if match[i] and s[i] == p[j]:
                        trans[i+1] = True
                match = trans
        
        return match[-1]
                        