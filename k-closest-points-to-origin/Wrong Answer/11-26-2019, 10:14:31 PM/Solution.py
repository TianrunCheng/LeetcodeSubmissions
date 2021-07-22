// https://leetcode.com/problems/k-closest-points-to-origin

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        len_dic = {}
        distances = []
        for _ in points:
            _len = _[0]^2+_[1]^2
            len_dic[_len] = _
            distances.append(_len)
        
        distances.sort()
        
        res = []
        
        for i in range(K):
            res.append(len_dic[distances[i]])
            
        return res