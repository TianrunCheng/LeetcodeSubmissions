// https://leetcode.com/problems/combination-sum-ii

# 134ms
# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort(reverse=True)
        
        
#         def fn(candi: List[int], target: int) -> List[List[int]]:
#             if target==0:
#                 return [[]]
#             elif target < 0:
#                 return None
#             elif len(candi) == 1:
#                 if target == candi[0]: return [[candi[0]]]
#                 else: return None
#             elif len(candi) > 1:
#                 sub_ans1 = fn(candi[1:], target-candi[0])
#                 sub_ans2 = fn(candi[1:], target)
#                 if sub_ans1==None:
#                     return sub_ans2
#                 else:
#                     for _ in sub_ans1:
#                         _.append(candi[0])
#                     if sub_ans2 == None:
#                         return sub_ans1
#                     else:
#                         for _ in sub_ans2:
#                             sub_ans1.append(_)
#                         return sub_ans1
        
#         ans = fn(candidates, target)
        
#         if ans == [[]] or ans == None:
#             return []
#         else:
#             i = 0
#             while (i < (len(ans)-1)):
#                 j = i +1
#                 while(j<len(ans)):
#                     if ans[j] == ans[i]:
#                         ans.pop(j)
#                     else:
#                         j = j + 1
#                 i = i+1
#             return ans

# 44ms
# class Solution:
#     def combinationSum2(self, C: List[int], t: int) -> List[List[int]]:
#         L, A, _ = len(C), [], C.sort()                          
#         def dfs(I, P, S):
#             if S == t: return A.append(P)
#             for i in range(I,L):
#                 if i > I and C[i] == C[i - 1]: continue
#                 if S + C[i] > t: break
#                 dfs(i + 1, P + [C[i]], S + C[i])
#         dfs(0, [], 0)
#         return A

# 44ms
# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
#         candidates.sort()
        
#         def fn(nums, x, i=0):
#             """backtracking algorithm"""
#             for k in range(i, len(candidates)): 
#                 if k > i and candidates[k] == candidates[k-1]: continue #break repetition 
#                 if candidates[k] > x: break 
#                 elif candidates[k] == x: ans.append(nums + [candidates[k]])
#                 else: fn(nums + [candidates[k]], x - candidates[k], k+1) #break repetition
        
#         ans = []
#         fn([], target)
#         return ans 

class Solution:
    def dfs(self, candidates, path, target, ret):
        n = len(candidates)
        if n == 0 or target < candidates[0]:
            return
        i = n - 1
        while i >= 0:
            while 0 <= i < n - 1 and candidates[i] == candidates[i + 1]:
                i -= 1
            if i == -1:
                return
            if candidates[i] == target:
                ret.append([candidates[i]] + path)
            elif candidates[i] < target:
                self.dfs(candidates[:i], [candidates[i]] + path, target - candidates[i], ret)
            i -= 1
        return



    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates, ret = sorted(candidates), []
        self.dfs(candidates, [], target, ret)
        return ret