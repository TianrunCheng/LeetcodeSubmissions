// https://leetcode.com/problems/check-if-n-and-its-double-exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        h = {}
        d = {}
        for i in range(len(arr)):
            print(h)
            print(d)
            if arr[i] * 2 in h:
                return True
            if arr[i] in h:
                return True
            d[arr[i]*2] = 0
            h[arr[i]] = 0
            
        return False