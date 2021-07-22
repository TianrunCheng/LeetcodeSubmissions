// https://leetcode.com/problems/check-if-n-and-its-double-exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        h = dict()
        for i in range(len(arr)):
            # print(h)
            if arr[i]*2 in h:
                return True
            elif arr[i] % 2 == 0 and (arr[i] // 2) in h:
                return True
            else:
                h[arr[i]] = 0
                h[arr[i] * 2] = 0
        return False