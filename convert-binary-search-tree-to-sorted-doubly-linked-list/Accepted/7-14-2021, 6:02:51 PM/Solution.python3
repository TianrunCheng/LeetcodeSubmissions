// https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # if we're allowed to use O(n) extra space, 
        # we could store the tree nodes in a dictionary
        # for they all have diff vals. then link them accordingly
        if not root:
            return root
        
        # if we don't use linear extra space: recursion?
        def recur(root: 'Node') -> ('Node', 'Node'):
            # rebuild the BST of root to a doubly linked list in place
            # return the [head, tail] of the rebuilt list
            
            if root.left:
                l_head, l_tail = recur(root.left)
                head = l_head
                l_tail.right = root
                root.left = l_tail
            else:
                head = root
                
            if root.right:
                r_head, r_tail = recur(root.right)
                tail = r_tail
                r_head.left = root
                root.right = r_head
            else:
                tail = root
            
            return (head, tail)
        
        head, tail = recur(root)
        head.left = tail
        tail.right = head
        return head