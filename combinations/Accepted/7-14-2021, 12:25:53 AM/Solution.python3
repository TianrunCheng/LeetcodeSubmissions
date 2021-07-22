// https://leetcode.com/problems/combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        backtrack()
        return output



# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         res = []
#         def recur(n: int, k: int) -> List[List[int]]:
#             # generator of all combinations (1, ..., n) choose k
#             # print("generate n = " + str(n) + ", k = " + str(k))
#             if n == k:
#                 res = []
#                 for i in range(1, n + 1):
#                     res.append(i)
#                 return [res]
            
#             if k == 1:
#                 res = []
#                 for i in range(1, n + 1):
#                     res.append([i])
#                 return res
            
#             n -= 1
#             k -= 1
#             res = []
#             for i in range(k, n + 1):
#                 sub = recur(i, k)
#                 for lis in sub:
#                     lis.append(i+1)
#                     res.append(lis)
#             return res
        
#         # for lis in recur(n, k):
#         #     print(lis)
#         #     res.append(lis)
#         return recur(n, k)
                    