// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        
        # let's search for the first position
        lo = 0
        hi = n - 1
        first = -1
        while(lo <= hi):
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] < target:
                    first = mid
                    break
                hi = mid - 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        if first < 0:
            return [-1, -1]
        
        
        # let's search for the last position
        lo = 0
        hi = n - 1
        last = -1
        while(lo <= hi):
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                if hi == n-1 or nums[mid+1] > target:
                    last = mid
                    break
                lo = mid + 1
        
        return [first, last]