// https://leetcode.com/problems/k-closest-points-to-origin

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        distances = []
        for _ in points:
            _len = _[0]^2+_[1]^2
            
            distances.append(_len)
        
        distances.sort()
        
        res = []
        
        for _ in points:
            if _[0]^2+_[1]^2 <= distances[K-1]:
                res.append(_)
            
        return res