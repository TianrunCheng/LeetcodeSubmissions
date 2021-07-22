// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def fn(nums: List[int]) -> List[List[int]]:
            if len(nums) == 1:
                return [[], nums]
            elif len(nums) > 1:
                ans = []
                sub_ans = fn(nums[1:])
                # print(sub_ans)
                for _ in sub_ans:
                    ans.append(_)
                print(sub_ans)
                print(ans)
                for _ in sub_ans:
                    seq = []
                    for j in _:
                        seq.append(j)
                    seq.append(nums[0])
                    ans.append(seq)
                print(ans)
                return ans
        
        return fn(nums)