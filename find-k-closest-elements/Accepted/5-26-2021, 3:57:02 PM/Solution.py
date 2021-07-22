// https://leetcode.com/problems/find-k-closest-elements

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        beg = k
        end = len(arr)
        # binary search looking for the ([start, ..., fin]) fin for the k-sub_array
        #                            [beg,..., ...  , mid, ..., end]
        #                                [b, ...,     ,a]
        while beg < end:
            mid = (beg+end) // 2
            a = arr[mid]
            b = arr[mid-k]
            if (a-x) >= (x-b):
                end = mid
            else:
                beg = mid + 1
        return arr[beg-k:end]             