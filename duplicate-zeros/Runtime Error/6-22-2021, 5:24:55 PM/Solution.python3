// https://leetcode.com/problems/duplicate-zeros

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
#         n = len(arr)
#         i = 0
#         while(i < n):
#             if arr[i] == 0:
#                 for j in range(n-2, i-1, -1):
#                     arr[j+1] = arr[j]
#                 i += 1
#             i += 1
        
#         return


        # find out how many elements are pushed out of edge
        n = len(arr)
        first_discard = n
        # first_discard initialized as arr[n]
        used_len = 0
        
        # traverse the arr, remember curr_len of the travelled array
        # - after duplicating zeros
        for i in range(n):
            if used_len >= n:
                first_discard = i
                # print(used_len)
                # print(first_discard)
                break
            
            if arr[i] == 0:
                used_len += 2
            else:
                used_len += 1
        
        left = first_discard - 1
        right = used_len - 1
        while(right > left and left >= 0):
            # print(arr)
            if arr[left] == 0:
                if right < n:
                    arr[right] = 0
                    right -= 1
                    arr[right] = 0
                    right -= 1
                    left -= 1
                else:
                    arr[right] = arr[left]
                    left -= 1
                    right -= 1
                    
            else:
                arr[right] = arr[left]
                right -= 1
                left -= 1
                
        return
                
        