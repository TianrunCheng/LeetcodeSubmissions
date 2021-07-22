// https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if right < 1:
            return 0
        
        # [left, right] is the range of appearing of a possible peak element
        # by keeping: nums[left-1] < nums[left] and nums[right] > nums[right+1] at all times
        # we guarantee there exist a peak in range [left, right]
        while( left < right ):
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        
        return left
            