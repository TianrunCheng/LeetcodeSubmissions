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
                yield None
                # return
                # return [None,]
            
            # res = []
            for i in range(start, end+1):
                # left tree [start, i-1], right tree [i+1, end]
                
                for l in build(start, i-1):
                    # print(l)
                    for r in build(i+1, end):
                        # print(r)
                        root = TreeNode(i)
                        root.left, root.right = l, r
                        yield root
            #             res.append(temp)
            # return res
        
        res = []
        iter_obj = build(1, n)
        
        for ele in iter_obj:
            res.append(ele)
        
        return res
        # return build(1, n) if n else []
        # #   # "if n else []" saves a lot of runtime, why?