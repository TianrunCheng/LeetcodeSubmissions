// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        ind = 0
        n = len(nums)
        
        while(ind <= reachable):
            reachable = max(reachable, nums[ind]+ind)
            if reachable >= (n-1):
                return True
            ind += 1
        
        return False
        