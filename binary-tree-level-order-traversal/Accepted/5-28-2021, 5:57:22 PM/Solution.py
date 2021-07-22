// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        res = []
        
        if root == None:
            return []
        
        queue.append(root)
        
        while(len(queue) > 0):
            n = len(queue)
            line = []
            for i in range(n):
                node = queue.pop(0)
                line.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            res.append(line)
        
        return res
        
        
            