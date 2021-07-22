// https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        
        i = -1
        j = 0
        # i: the next to merge in nums1, stored in nums2[i] when j > 0
        # j: the next to merge in nums2, stored in nums2[j]
        
        for k in range(m + n):
            print(nums1)
            print(nums2)
            print("k = " + str(k))
            if i == -1:
                print("i==-1")
                if k < m:
                    if nums1[k] <= nums2[j]:
                        pass
                    else:
                        swap = nums1[k]
                        nums1[k] = nums2[j]
                        nums2[j] = swap
                        i = j
                        j += 1
                else:
                    nums1[k] = nums2[j]
                    j += 1
            elif j < n:
                print("i=" + str(i) + "; j=" + str(j))
                if nums2[i] > nums2[j]:
                    swap = nums1[k]
                    nums1[k] = nums2[j]
                    nums2[j] = swap
                    j += 1
                elif k < m:
                    swap = nums1[k]
                    nums1[k] = nums2[i]
                    nums2[i] = swap
                else:
                    nums1[k] = nums2[i]
                    i = -1
            else:
                if k > m:
                    nums1[k] = nums2[i]
                    i += 1
                else:
                    swap = nums1[k]
                    nums1[k] = nums2[i]
                    nums2[i] =swap
            
            print()
        return
                    
                
        
        
        
        
        
        
# XXXXX this is a first try wrong solution XXXXX
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

        
        
            
        