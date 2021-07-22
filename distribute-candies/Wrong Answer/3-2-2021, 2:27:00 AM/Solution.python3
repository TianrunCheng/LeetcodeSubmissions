// https://leetcode.com/problems/distribute-candies

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = set()
        n = len(candyType)
        for c in candyType:
            types.add(c)
        t = len(types)
        if t < n/2:
            return t
        else:
            return n/2
        