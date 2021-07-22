// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        right_max = -1
        
        for i in range(n-1, -1, -1):
            swap = arr[i]
            arr[i] = right_max
            if swap > right_max:
                right_max = swap
        
        return arr