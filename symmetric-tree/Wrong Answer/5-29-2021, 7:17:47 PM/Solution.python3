// https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def sameTree(tree1: TreeNode, tree2: TreeNode) -> bool:
            if tree1 == None and tree2 == None:
                return True
            elif tree2 == None or tree1 == None:
                return False
            else:
                if tree1.val == tree2.val:
                    return sameTree(tree1.left, tree2.left) and sameTree(tree1.right, tree2.right)
                else:
                    return False
        
        if root == None:
            return True
        
        return sameTree(root.left, root.right)
            