// https://leetcode.com/problems/same-tree

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        # iterative approach, Breadth First Search
        def sameNode(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
        
        dq = deque()
        dq.append((p, q))
        while(len(dq) > 0):
            curr_p, curr_q = dq.popleft()
            if not sameNode(curr_p, curr_q):
                return False
            if curr_p:
                dq.append((curr_p.left, curr_q.left))
                dq.append((curr_p.right, curr_q.right))
        return True
        
        
        
        
        
#         # recursive approach
#         if not p and not q:
#             return True
#         if not p or not q:
#             return False
#         if p.val != q.val:
#             return False
#         return self.isSameTree(p.left, q. left) and self.isSameTree(p.right, q.right)