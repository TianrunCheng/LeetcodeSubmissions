// https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        # https://www.geeksforgeeks.org/global-keyword-in-python/
        # global variable in nested functions
        def topDown(node: TreeNode, depth: int, ans: int) -> int:

            if node == None:
                return ans
            if node.left == None and node.right == None:
                if ans < depth:
                    ans = depth
                return ans
            l_ans = topDown(node.left, depth + 1, ans)
            r_ans = topDown(node.right, depth + 1, ans)
            ans = max(ans, l_ans, r_ans)
            return ans
        
        ans = topDown(root, 1, 0)
        
        return ans