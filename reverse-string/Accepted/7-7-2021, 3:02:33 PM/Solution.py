// https://leetcode.com/problems/reverse-string

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # exchange the first and last char each time
        def helper(start: int, end: int):
            # reverse s[start: end+1] in-place
            if end <= start:
                return
            swap = s[end]
            s[end] = s[start]
            s[start] = swap
            helper(start+1, end-1)
            
            return
        
        helper(0, len(s)-1)
        
        return
                