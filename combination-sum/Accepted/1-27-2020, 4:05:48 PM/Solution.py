// https://leetcode.com/problems/combination-sum

import math
# sort the set in descendent order [big->small]
# divide and conquer, for each candidate number, create i=1~floor(tar_curr/candi_curr) recurrent problems:
# sub_problem candidates being list of nums afer candi_curr and tar_curr = tar_curr - i*candi_curr
# boundary: len(candi_list) == 1, if target_current == some_int*candi_curr, return set[[candi_curr*some_int]]
# i_th resulting set = add i*candi_curr to each entrie of the subproblem return set
# resulting set: merge all floor(tar_curr/candi_curr) resulting sets into one set of number sequences

class Solution:
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort(reverse = True)
#         # ans = []
        
#         def fn(candi, target) -> [[int]]:
#             if target == 0:
#                 return [[]]
#             elif len(candi) == 1:
#                 if target % candi[0] == 0:
#                     ans = [[]]
#                     for _ in range(math.floor(target / candi[0])):
#                         ans[0].append(candi[0])
#                     return ans
#                 else:
#                     return [[]]
#             else:
#                 ans = [[]]
#                 for i in range(math.floor(target / candi[0])+1):
#                     sub_ans = fn(candi[1:], target - i * candi[0])
#                     # print(sub_ans)
#                     if sub_ans != [[]]:
#                         # print(sub_ans)
#                         for seq in sub_ans:
#                             for _ in range(i):
#                                 seq.append(candi[0])
#                             ans.append(seq)
#                     elif target == candi[0] * i:
#                         ans.append([])
#                         for _ in range(i):
#                             ans[-1].append(candi[0])
#                 ans.pop(0)
     
#                 return ans

#         ans = fn(candidates, target)
#         if ans==[[]]:
#             return []
#         else:
#             return ans
        def combinationSum(self, candidates, target):
            res = []
            candidates.sort()
            self.dfs(candidates, target, 0, [], res)
            return res

        def dfs(self, nums, target, index, path, res):
            if target < 0:
                return  # backtracking
            if target == 0:
                res.append(path)
                return 
            for i in range(index, len(nums)):
                self.dfs(nums, target-nums[i], i, path+[nums[i]], res)