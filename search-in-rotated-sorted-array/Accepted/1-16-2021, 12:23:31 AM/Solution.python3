// https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # 
        # """ 
        # Its interesting that this brute solution is faster than 75.5% = =
        # """
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1
        
        # How do you begin a binary search in a rotated array?
        n = len(nums)
        lo = 0
        hi = n - 1
        
        while(lo <= hi):
            mid = lo + (hi - lo)//2
            print(lo, mid, hi)
            if nums[lo] <= nums[mid] and nums[hi] <= nums[lo]:
                if target == nums[hi]:
                    return hi
                if target == nums[lo]:
                    return lo
                if target == nums[mid]:
                    return mid
                if target > nums[lo] and target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[hi] <= nums[lo] and nums[mid] <= nums[hi]:
                if target == nums[hi]:
                    return hi
                if target == nums[lo]:
                    return lo
                if target == nums[mid]:
                    return mid
                if target > nums[mid] and target < nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            elif nums[lo] <= nums[mid] and nums[mid] <= nums[hi]:
                if target == nums[hi]:
                    return hi
                if target == nums[lo]:
                    return lo
                if target == nums[mid]:
                    return mid
                if target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        return -1
                
        