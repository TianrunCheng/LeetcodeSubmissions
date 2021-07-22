// https://leetcode.com/problems/valid-mountain-array

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        
        i = 0
        j = n - 1
        # i: left index, ind <= i all strictly increasing
        # j: right index, ind >= j all strictly decreasing
        
        while(i < (n-1) and arr[i+1] > arr[i]):
            i += 1
        while(j > 0 and arr[j-1] > arr[j]):
            j -= 1
        
        if i == j and 0 < i and i < (n-1):
            return True
        
        return False
        
#         while(i < j):
#             if arr[i+1] > arr[i]:
#                 i += 1
#             elif arr[i+1] == arr[i]:
#                 return False
#             if arr[j-1] > arr[j]:
#                 j -= 1
#             elif arr[j-1] == arr[j]:
#                 return False
        
                