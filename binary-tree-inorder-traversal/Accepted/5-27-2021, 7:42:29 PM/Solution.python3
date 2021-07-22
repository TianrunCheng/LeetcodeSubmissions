// https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # iterative approach
        
        stack = []
        # stack only holds nodes we need to return to
        
        res = []

        curr = root
        
        while(curr != None or len(stack) > 0):
            
            if curr == None:
                curr = stack.pop(-1)
                # this node is a node popped from stack
                # meaning we have finished traversing its left branch
                res.append(curr.val)
                curr = curr.right
            
            else:
                if curr.left != None:
                    stack.append(curr)
                    curr = curr.left
                else:
                    res.append(curr.val)
                    curr = curr.right

        
        return res
        
        
        
# recursive solution:

#         res = []
        
#         def inorder(node: TreeNode):
#             if node == None:
#                 return
#             inorder(node.left)
#             res.append(node.val)
#             inorder(node.right)
        
#         inorder(root)
        
#         return res
        