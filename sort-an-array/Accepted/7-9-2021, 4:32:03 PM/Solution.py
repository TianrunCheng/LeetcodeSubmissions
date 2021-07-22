// https://leetcode.com/problems/sort-an-array

class Solution:
    def merge(self, left, right):
        res = []
        left_cursor = right_cursor = 0
        
        while left_cursor < len(left) and right_cursor < len(right):
            if left[left_cursor] > right[right_cursor]:
                res.append(right[right_cursor])
                right_cursor += 1
            else:
                res.append(left[left_cursor])
                left_cursor += 1
                
        res.extend(right[right_cursor:])
        res.extend(left[left_cursor:])
        return res
        
    
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if len(nums) < 2:
            return nums
        left = self.sortArray(nums[:(n // 2)])
        right = self.sortArray(nums[(n // 2):])
        return self.merge(left, right)