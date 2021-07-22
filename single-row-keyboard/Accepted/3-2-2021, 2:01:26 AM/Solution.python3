// https://leetcode.com/problems/single-row-keyboard

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dic = {}
        for i in range(len(keyboard)):
            dic[keyboard[i]] = i
        
        tot = 0
        curr = 0
        for w in word:
            tot += abs(dic[w]-curr)
            curr = dic[w]
        return tot
        