// https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    global ans
    ans = 0
    def maxDepth(self, root: TreeNode) -> int:
        
        
        # https://www.geeksforgeeks.org/global-keyword-in-python/
        # global variable in nested functions
        def topDown(node: TreeNode, depth: int):
            global ans
            if node == None:
                return
            if node.left == None and node.right == None:
                if ans < depth:
                    ans = depth
            topDown(node.left, depth + 1)
            topDown(node.right, depth + 1)
        
        topDown(root, 1)
        
        return ans-1