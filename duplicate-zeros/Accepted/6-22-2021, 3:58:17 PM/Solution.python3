// https://leetcode.com/problems/duplicate-zeros

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        while(i < n):
            if arr[i] == 0:
                for j in range(n-2, i-1, -1):
                    arr[j+1] = arr[j]
                i += 1
            i += 1
        
        return