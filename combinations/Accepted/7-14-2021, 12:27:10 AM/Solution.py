// https://leetcode.com/problems/combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # init first combination
        nums = list(range(1, k + 1)) + [n + 1]
        
        output, j = [], 0
        while j < k:
            # add current combination
            output.append(nums[:k])
            # increase first nums[j] by one
            # if nums[j] + 1 != nums[j + 1]
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1
            
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
                    