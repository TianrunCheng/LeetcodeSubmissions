// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
      
        n = len(nums)
        for i in range(len(nums)):
            nums[i] = i + nums[i]
        # print(nums)
        steps = 0
        i = 0
        greedy = 0
        while i < n-1:
            # if nums[i] >= n-1:
            #     break
            steps += 1
            greedy = 0
            for j in range(i+1, nums[i]+1):
                greedy = max(greedy, nums[j])
                # print(greedy)
            i = greedy
        steps += 1
        # print(steps)
        return steps