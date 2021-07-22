// https://leetcode.com/problems/find-k-closest-elements

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        
        left = 0
        right = len(arr) - 1
        
        while(left < right - 1):
            mid = (left + right) // 2
            if arr[mid] == x:
                left = right = mid
            elif arr[mid] < x:
                if arr[mid+1] > x:
                    left = mid
                    right = mid+1
                else:
                    left = mid + 1
            else:
                if arr[mid-1] < x:
                    left = mid-1
                    right = mid
                else:
                    right = mid-1

        
        for i in range(k):
            if 0 <= left and right <= len(arr) - 1:
                if (x - arr[left]) <= (arr[right] - x):
                    res.insert(0, arr[left])
                    if (left < right):
                        left = left - 1
                    else:
                        left -= 1
                        right += 1
                else:
                    res.append(arr[right])
                    right = right + 1
            elif left < 0:
                res.append(arr[right])
                right = right + 1
            else:
                res.insert(0, arr[left])
                left = left - 1
        
        return res
                