// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # corner cases, len <=2 
        
        left, right = 0, len(nums)-1
        
        while( left <= right ):
            mid = left + (right - left) // 2
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        

        if left > right:
            return [-1, -1]
        
        #  left ... start_ind, ..., mid, ..., end_ind, ..., right
        # [ 0, ..., 0, 1, 1,...,    1, ...,      1,   2, ...,   23 ]
        left_end = mid
        right_start = mid
        
        
        #  left, ... ,start, ..., left_end
        while(left < left_end):
            start = (left + left_end) // 2
            # print("left:" + str(left) + " start:" + str(start) + " left_end:" + str(left_end))
            if nums[start] < target:
                left = start + 1
            else:
                left_end = start
                
        start = left
        
        #  right_start, ..., end, ..., right
        while(right_start < right):
            end = (right_start + right) // 2 + 1
            # print("right_start:" + str(right_start) + " end:" + str(end) + " right:" + str(right))
            if nums[end] > target:
                right = end - 1
            else:
                right_start = end
        
        end = right
        
        return [start, end]
        
        
        