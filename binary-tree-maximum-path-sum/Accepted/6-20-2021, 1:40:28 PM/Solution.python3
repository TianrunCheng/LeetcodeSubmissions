// https://leetcode.com/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        global curr_max
        curr_max = -1000
        
        def maxBranch(root: TreeNode) -> int:
            global curr_max
            # maxBranch returns the maximum branch val stemming from root
            # including the root val
            if root == None:
                return 0
            left = maxBranch(root.left)
            right = maxBranch(root.right)
            # compute the max path passing through root
            curr = max(left+root.val, right+root.val, left+right+root.val, root.val)
            if curr > curr_max:
                curr_max = curr
            return max(left+root.val, right+root.val, root.val)
        
        branch = maxBranch(root)
        
        return curr_max