// https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
#         # https://www.geeksforgeeks.org/global-keyword-in-python/
#         # global variable in nested functions

#         global ans
#         # claim a global variable
#         ans = 0
        
#         # pass on the depth of the current node
#         def topDown(node: TreeNode, depth: int):
#             global ans
#             # referring a global variable
#             if node == None:
#                 return
#             if node.left == None and node.right == None:
#                 if ans < depth:
#                     ans = depth
#                 return
#             topDown(node.left, depth+1)
#             topDown(node.right, depth+1)
        
#         topDown(root, 1)
        
#         return ans


#         # bottom-up recursive func
#         if root == None:
#             return 0
#         l = self.maxDepth(root.left)
#         r = self.maxDepth(root.right)
#         return max(l, r) + 1

        # iterative solution
        ans = 0
        stack = []
        
        if root == None:
            return 0
        
        root.val = 1
        stack.append(root)
        
        
        while(len(stack) > 0):
            node = stack.pop(-1)
            level = node.val
            if node.left == None and node.right == None:
                ans = max(level, ans)
            if node.right != None:
                node.right.val = level + 1
                stack.append(node.right)
            if node.left != None:
                node.left.val = level + 1
                stack.append(node.left)
        
        return ans

            




#         # avoid using global variable, pass on the val of global each time

#         def topDown(node: TreeNode, depth: int, ans: int) -> int:

#             if node == None:
#                 return ans
#             if node.left == None and node.right == None:
#                 if ans < depth:
#                     ans = depth
#                 return ans
#             l_ans = topDown(node.left, depth + 1, ans)
#             r_ans = topDown(node.right, depth + 1, ans)
#             ans = max(ans, l_ans, r_ans)
#             return ans
        
#         ans = topDown(root, 1, 0)
        
#         return ans

