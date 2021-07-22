// https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
#         def symTree(tree1: TreeNode, tree2: TreeNode) -> bool:
#             if tree1 == None and tree2 == None:
#                 return True
#             elif tree2 == None or tree1 == None:
#                 return False
#             else:
#                 if tree1.val == tree2.val:
#                     return symTree(tree1.left, tree2.right) and symTree(tree1.right, tree2.left)
#                 else:
#                     return False
        
#         if root == None:
#             return True
        
#         return symTree(root.left, root.right)
        
        # iterative solution
        # left traverse left subtree == right traverse right subtree?
        # will not work. 
        # use level first traversal
        if root == None:
            return True
        lq = []
        rq = []
        lq.append(root.left)
        rq.append(root.right)
        
        while(len(lq) > 0):
            if len(rq) == 0:
                return False
            lnode = lq.pop(-1)
            rnode = rq.pop(-1)
            if lnode == None and rnode == None:
                continue
            if lnode == None or rnode == None:
                return False
            if lnode.val == rnode.val:
                lq.append(lnode.left)
                lq.append(lnode.right)
                rq.append(rnode.right)
                rq.append(rnode.left)
        
        if len(rq) == 0:
            return True
        
        return False
        
        
        
        

    
    
    