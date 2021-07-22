// https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        for k in range(m + n - 1, -1, -1):
            if i >= 0 and i < m and j >= 0 and j < n:
                if nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
            elif i >= 0 and i < m:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
        return
        
        
        

#       # XXXXXXX this is a second try wrong solution. XXXXXXXXX
#       # didn't think through and started working on the code
#       # the solution tries to move and merge items from left to right
#         if n == 0:
#             return
        
#         i = -1
#         n1 = 0
#         # n1: the times we withdraw from nums1
#         j = 0
#         # i: the next to merge in nums1, stored in nums2[i] when j > 0
#         # j: the next to merge in nums2, stored in nums2[j]
        
#         for k in range(m + n):
#             print(nums1)
#             print(nums2)
#             print("k = " + str(k))
#             if i == -1:
#                 print("i==-1")
#                 if k < m:
#                     if nums1[k] <= nums2[j]:
#                         n1 += 1
#                     else:
#                         swap = nums1[k]
#                         nums1[k] = nums2[j]
#                         nums2[j] = swap
#                         i = j
#                         j += 1
#                 else:
#                     nums1[k] = nums2[j]
#                     j += 1
#             elif j < n:
#                 print("i=" + str(i) + "; j=" + str(j))
#                 if nums2[i] > nums2[j]:
#                     swap = nums1[k]
#                     nums1[k] = nums2[j]
#                     nums2[j] = swap
#                     j += 1
#                 elif k < m:
#                     swap = nums1[k]
#                     nums1[k] = nums2[i]
#                     nums2[i] = swap
#                     n1 += 1
#                 else:
#                     nums1[k] = nums2[i]
#                     if n1 < m:
#                         i += 1
#                         n1 += 1
#                     else:
#                         i = -1
#             else:
#                 if k >= m:
#                     nums1[k] = nums2[i]
#                     n1 += 1
#                     i += 1
#                 else:
#                     swap = nums1[k]
#                     nums1[k] = nums2[i]
#                     nums2[i] =swap
#                     n1 += 1
            
#             print()
#         return
                    
                
        
        
        
        
        
        
#       # XXXXX this is a first try wrong solution XXXXX
#         j = 0
        
#         # remember to discuss corner case where nums1[i], nums2[j] does not exist
        
#         for i in range(m+n):
#             print(nums1)
#             print(nums2)
#             if j >= n:
#                 return
#             if i < m:
#                 if nums1[i] > nums2[j]:
#                     swap = nums1[i]
#                     nums1[i] = nums2[j]
#                     nums2[j] = swap
#                     j += 1
#             else:
#                 nums1[i] = nums2[j]
#                 j += 1
        
#         return

        
        
            
        