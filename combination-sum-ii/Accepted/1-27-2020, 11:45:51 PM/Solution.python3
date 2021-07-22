// https://leetcode.com/problems/combination-sum-ii

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        
        
        def fn(candi: List[int], target: int) -> List[List[int]]:
            if target==0:
                return [[]]
            elif target < 0:
                return None
            elif len(candi) == 1:
                if target == candi[0]: return [[candi[0]]]
                else: return None
            elif len(candi) > 1:
                sub_ans1 = fn(candi[1:], target-candi[0])
                sub_ans2 = fn(candi[1:], target)
                if sub_ans1==None:
                    return sub_ans2
                else:
                    for _ in sub_ans1:
                        _.append(candi[0])
                    if sub_ans2 == None:
                        return sub_ans1
                    else:
                        for _ in sub_ans2:
                            sub_ans1.append(_)
                        return sub_ans1
        
        ans = fn(candidates, target)
        
        if ans == [[]] or ans == None:
            return []
        else:
            i = 0
            while (i < (len(ans)-1)):
                j = i +1
                while(j<len(ans)):
                    if ans[j] == ans[i]:
                        ans.pop(j)
                    else:
                        j = j + 1
                i = i+1
            return ans
        
                