// https://leetcode.com/problems/count-univalue-subtrees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        global res
        res = 0
        
        if root == None:
            return 0
        
        # num of unival subtree can come up with a post-order traversal of the tree
        # leaf nodes are all unival subtrees
        # if left.val == right.val == root.val root is also a unival subree
        def postorder(root: TreeNode) -> bool:
            global res
            if root.left == None and root.right == None:
                res += 1
                return True
            lflag = False
            rflag = False
            if root.left != None:
                lflag = True
                l = postorder(root.left)
                lval = root.left.val
            if root.right != None:
                rflag = True
                r = postorder(root.right)
                rval = root.right.val
            if lflag and rflag:
                if l and r and lval == rval and lval == root.val:
                    res += 1
                    return True
                else:
                    return False
            elif lflag:
                if l and lval == root.val:
                    res += 1
                    return True
                else:
                    return False
            else:
                if r and rval == root.val:
                    res += 1
                    return True
                else:
                    return False
        
        postorder(root)
        
        return res

                
            
            