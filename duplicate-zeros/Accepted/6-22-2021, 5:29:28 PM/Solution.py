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


#         # find out how many elements are pushed out of edge
#         n = len(arr)
#         first_discard = n
#         # first_discard initialized as arr[n]
#         used_len = 0
        
#         # traverse the arr, remember curr_len of the travelled array
#         # - after duplicating zeros
#         for i in range(n):
#             if used_len >= n:
#                 first_discard = i
#                 print(used_len)
#                 print(first_discard)
#                 break
            
#             if arr[i] == 0:
#                 used_len += 2
#             else:
#                 used_len += 1
        
#         left = first_discard - 1
#         right = used_len - 1
#         while(right > left):
#             print(left)
#             print(right)
#             # print(arr)
#             if arr[left] == 0:
#                 if right < n:
#                     arr[right] = 0
#                     right -= 1
#                     arr[right] = 0
#                     right -= 1
#                     left -= 1
#                 else:
#                     right -= 1
#                     arr[right] = arr[left]
#                     left -= 1
#                     right -= 1
                    
#             else:
#                 arr[right] = arr[left]
#                 right -= 1
#                 left -= 1
                
#         return


        possible_dups = 0
        length_ = len(arr) - 1

        # Find the number of zeros to be duplicated
        for left in range(length_ + 1):

            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if left > length_ - possible_dups:
                break

            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included  
                if left == length_ - possible_dups:
                    arr[length_] = 0 # For this zero we just copy it without duplication.
                    length_ -= 1
                    break
                possible_dups += 1

        # Start backwards from the last element which would be part of new list.
        last = length_ - possible_dups

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]
        