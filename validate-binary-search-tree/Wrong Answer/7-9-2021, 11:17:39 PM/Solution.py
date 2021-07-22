// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.valid = True
        # define a helper function, returning min and max of each subtree
        
        def checkSubTree(root: TreeNode) -> (int, int):
            # return (min_val, max_val)
            if not self.valid:
                # no need to check anything, tree is invalid
                return (0, 0)
            
            res = [root.val, root.val]
            if not root.left and not root.right:
                # no branches, we've reached a leaf
                return (res[0], res[1])
            if root.left:
                l_min, l_max = checkSubTree(root.left)
                if l_max > root.val:
                    self.valid = False
                    return (0,0)
                res[0] = l_min
            if root.right:
                r_min, r_max = checkSubTree(root.right)
                if r_min < root.val:
                    self.valid = False
                    return (0, 0)
                res[1] = r_max
            return (res[0], res[1])
        
        checkSubTree(root)
        
        return self.valid
                