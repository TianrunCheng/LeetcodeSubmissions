// https://leetcode.com/problems/binary-tree-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # iterative solution
        stack = []
        res = []
        
        if root != None:
            stack.append(root)
        
        while(len(stack) > 0):
            node = stack.pop(-1)
            res.append(node.val)
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)
        
        return res
        
        
        
        
        
        
        
        # recursive solution
#         res = []
        
#         def preorder(node: TreeNode):
#             if node == None:
#                 return
#             res.append(node.val)
#             preorder(node.left)
#             preorder(node.right)
#             return
        
#         preorder(root)
        
#         return res
