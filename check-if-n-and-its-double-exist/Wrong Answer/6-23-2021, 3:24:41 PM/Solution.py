// https://leetcode.com/problems/check-if-n-and-its-double-exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dic = {}
        for num in arr:
            if num not in dic:
                dic[num] = 0
        for num in arr:
            tar = num * 2
            if tar in dic:
                return True
        return False