// https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        curr_max = 0
        if len(height) < 2:
            return 0
        
        for i in range(len(height)):
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