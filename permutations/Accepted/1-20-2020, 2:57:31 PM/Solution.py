// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        def fn(nums: List[int]) -> List[List[int]]:
            if len(nums) == 1:
                return [nums]
            else:
                ans = []
                for i in range(len(nums)):
                    num = []
                    for j in range(len(nums)):
                        if j != i:
                            num.append(nums[j])
                    sub_ans = fn(num)
                    for _ in sub_ans:
                        _.append(nums[i])
                        ans.append(_)
                return ans
        
        
        ans = fn(nums)
        return ans