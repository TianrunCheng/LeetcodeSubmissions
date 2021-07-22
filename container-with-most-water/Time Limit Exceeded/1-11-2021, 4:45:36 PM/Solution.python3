// https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
    
        """
        Brute Force: O(n^2) average case
        Note: n -> 3 * 10^4, too large
        """

        curr_max = 0
        if len(height) < 2:
            return 0
        
        for i in range(len(height)):
            if height[i] is 0:
                continue
            if i>0 and height[i] <= height[i-1]:
                continue
            if (curr_max / height[i]) > (len(height)-1-i):
                continue
            else:
                for j in range(i+1, len(height)):
                    container = (j - i) * min(height[i], height[j])
                    # print(container)
                    if curr_max > container:
                        pass
                    else:
                        curr_max = container
        
        return curr_max


