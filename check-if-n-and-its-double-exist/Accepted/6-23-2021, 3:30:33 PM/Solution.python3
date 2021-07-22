// https://leetcode.com/problems/check-if-n-and-its-double-exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        h = dict()
        for i in range(len(arr)):
            if arr[i]*2 in h or arr[i] in h.values():
                return True
            else:
                h[arr[i]] = arr[i]*2
        return False