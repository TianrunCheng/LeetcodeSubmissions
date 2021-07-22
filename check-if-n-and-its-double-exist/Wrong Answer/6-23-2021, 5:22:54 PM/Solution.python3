// https://leetcode.com/problems/check-if-n-and-its-double-exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        h = {}
        d = {}
        for i in range(len(arr)):
            if arr[i] in d:
                return True
            if arr[i] % 2 == 0 and arr[i] // 2 in h:
                return True
            d[arr[i]*2] = 0
            h[arr[i]] = 0
            
        return False