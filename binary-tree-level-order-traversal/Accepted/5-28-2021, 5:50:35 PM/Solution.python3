// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        currlevel = []
        res = []
        
        if root == None:
            return []
        
        currlevel.append(root)
        
        while(len(currlevel) > 0):
            nextlevel = []
            line = []
            for node in currlevel:
                line.append(node.val)
                if node.left != None:
                    nextlevel.append(node.left)
                if node.right != None:
                    nextlevel.append(node.right)
            currlevel = nextlevel
            res.append(line)
        
        return res
        
        
            