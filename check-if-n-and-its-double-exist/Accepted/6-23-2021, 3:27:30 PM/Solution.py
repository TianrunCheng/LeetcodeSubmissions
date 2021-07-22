// https://leetcode.com/problems/check-if-n-and-its-double-exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dic = {}
        
        for num in arr:
            if num not in dic:
                dic[num] = 0
        
        for num in arr:
            tar = num * 2
            if tar in dic and tar != 0:
                return True
        
        if 0 in dic:
            count = 0
            for num in arr:
                if num == 0:
                    count += 1
            if count > 1:
                return True
        
        return False