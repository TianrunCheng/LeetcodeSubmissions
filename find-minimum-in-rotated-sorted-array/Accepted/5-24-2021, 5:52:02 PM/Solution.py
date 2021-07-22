// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # keep search range [left, right] more than 2 elements, mid index round down
        # find the "sharp drop" point in range [left, right], 
        # if nums[mid] > nums[right], eliminate left half along with mid ele
        # if nums[mid] < nums[right], eliminate right half without the mid ele
        
        left = 0
        right = len(nums) - 1
        
        if right < 1:
            return nums[0]
        
        while(left < right):
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]