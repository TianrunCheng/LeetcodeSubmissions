// https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        stack = []
        
        if root == None:
            return False
        
        stack.append((root, root.val))
        
        while(len(stack) > 0):
            (node, val) = stack.pop(-1)
            if node.left == None and node.right == None:
                if val == targetSum:
                    return True
            if node.right != None:
                stack.append((node.right, val + node.right.val))
            if node.left != None:
                stack.append((node.left, val + node.left.val))
        
        return False