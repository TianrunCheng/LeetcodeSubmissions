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
        
        res = []
        
#         if root == None:
#             return res
        
#         flag = False
        curr = root
        
        while(curr != None or len(stack) > 0):
            # print(curr.val)
            # print(stack)
            if curr == None:
                curr = stack.pop(-1)
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
        