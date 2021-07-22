// https://leetcode.com/problems/find-the-celebrity

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        x = 0
        for i in range(1, n):
            # n questions to find possible celebrity
            if knows(x, i):
                # x knows i, x is not cele
                x = i
            else:
                # x doesn't know i, i is not cele
                pass
        
        cele = x
        for i in range(n):
            if i is not cele:
                if not knows(i, cele):
                    return -1
        return cele