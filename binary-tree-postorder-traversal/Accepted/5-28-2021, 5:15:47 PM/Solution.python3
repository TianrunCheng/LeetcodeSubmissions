// https://leetcode.com/problems/binary-tree-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        # iterative solution:
        
        res = []
        s1 = []
        # the "to-do-list"
        s2 = []
        # when we meet a node with branches attached
        # if it "has been" under other elements in s1, 
        # we only output its value (its left and right outputted)
        
        if root == None:
            return res
        
        s1.append(root)
        
        while(len(s1) > 0):
            curr = s1[-1]
            if len(s2) > 0 and s2[-1] == curr:
                res.append(curr.val)
                s1.pop(-1)
                s2.pop(-1)
            else:
                flag = False
                if curr.right != None:
                    s1.append(curr.right)
                    flag = True
                if curr.left != None:
                    s1.append(curr.left)
                    flag = True
                if flag:
                    s2.append(curr)
                else:
                    res.append(curr.val)
                    s1.pop(-1)
                    
        return res
        
        
        
        
        
        
        
                
# recursive solution:

#         res = []
        
#         def postorder(node: TreeNode):
#             if node == None:
#                 return
#             postorder(node.left)
#             postorder(node.right)
#             res.append(node.val)
            
#         postorder(root)
        
#         return res