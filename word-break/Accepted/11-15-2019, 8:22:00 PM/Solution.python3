// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        results = [False for i in range(n+1)]
        results[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if results[j] == True and s[j:i] in wordDict:
                    results[i] = True
        return results[n]
                
        