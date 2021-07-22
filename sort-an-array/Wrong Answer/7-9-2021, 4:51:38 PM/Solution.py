// https://leetcode.com/problems/sort-an-array

class Solution:
    
    # implement bottom-up solution
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        size = 1
        # size of sorted sub_arrays in each pass
        while (2 * size) <= n:
            for cursor in range(0, n, 2 * size):
                nums[cursor: min(cursor + 2* size, n)] = self.merge(nums[cursor: cursor + size], nums[cursor+size: min(cursor + 2 * size, n)])
            
            size = size * 2
        return nums
        
        
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
        
    
#     # rewrite top-down solution    
#     def sortArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         if len(nums) < 2:
#             return nums
#         left = self.sortArray(nums[:(n // 2)])
#         right = self.sortArray(nums[(n // 2):])
#         return self.merge(left, right)