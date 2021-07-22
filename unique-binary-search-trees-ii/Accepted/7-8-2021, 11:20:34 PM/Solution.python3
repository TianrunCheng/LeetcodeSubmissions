// https://leetcode.com/problems/unique-binary-search-trees-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        def build(start: int, end: int):
            # a generator of all binary trees storing vals between [start: end]
            
            if start > end:
                # yield None
                return [None]
            
            res = []
            for i in range(start, end+1):
                # left tree [start, i-1], right tree [i+1, end]
                left = build(start, i-1)
                right = build(i+1, end)
                for l in left:
                    # print(l)
                    for r in right:
                        # print(r)
                        temp = TreeNode(i)
                        temp.left = l
                        temp.right = r
                        # yield temp
                        res.append(temp)
            return res
        
#         res = []
#         iter_obj = build(1, n)
        
#         for ele in iter_obj:
#             res.append(ele)
        
        # return res
        return build(1, n)