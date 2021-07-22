// https://leetcode.com/problems/trapping-rain-water

"""
the height of water of a certain x-coordinate is decided by:
the shorter of the left and right height of elevation one can see from this site x
which is the highest elevation to its left and the highest elevation to its right

Calculating from the two end: recording the highest seen so far from left and right
When curr_left_most <= curr_right_most:
walk one step from left, 
    if site x: height[x] <= known_left_most < curr_right_most:
        water level of that site = known_left_most - height[x] , walk one more step
    if site x: height[x] > known_left_most:
        known_left_most = height[x], no water
Right side walking are symmetrical
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        width = len(height)
        right = width - 1
        left = 0
        water = 0
        l_most = height[left]
        r_most = height[right]
        while right > (left + 1):
            if l_most <= r_most:
                left += 1
                if height[left] <= l_most:
                    water += l_most - height[left]
                else:
                    l_most = height[left]
            else:
                right -= 1
                if height[right] <= r_most:
                    water += r_most - height[right]
                else:
                    r_most = height[right]
        
        return water