// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        val = preorder[0]
        root = TreeNode(val)
        cut = inorder.index(val)
        root.left = self.buildTree(preorder[1:cut+1], inorder[:cut])
        root.right = self.buildTree(preorder[cut+1:], inorder[cut+1:])
        
        return root