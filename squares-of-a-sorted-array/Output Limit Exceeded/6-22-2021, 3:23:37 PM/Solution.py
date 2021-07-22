// https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # find the first non-negative number's index
        n = len(nums)
        turning = n
        for i in range(n):
            if nums[i] >= 0:
                turning = i
                break
        res = []
        left = turning - 1
        right = turning
        for i in range(n):
            nums[i] = nums[i] ** 2
            
        while(left >= 0 or right < n):
            print(res)
            if left >= 0 and right < n:
                if nums[left] < nums[right]:
                    res.append(nums[left])
                    left -= 1
                else:
                    res.append(nums[right])
                    right += 1
            elif left < 0:
                res.append(nums[right])
                right += 1
            else:
                res.append(nums[left])
                left -= 1
        
        return res
                