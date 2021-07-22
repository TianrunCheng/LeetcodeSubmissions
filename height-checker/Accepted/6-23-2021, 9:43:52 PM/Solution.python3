// https://leetcode.com/problems/height-checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        copy = []
        for h in heights:
            copy.append(h)
        
        copy.sort()
        
        count = 0
        for i in range(len(heights)):
            if copy[i] != heights[i]:
                count += 1
        
        return count