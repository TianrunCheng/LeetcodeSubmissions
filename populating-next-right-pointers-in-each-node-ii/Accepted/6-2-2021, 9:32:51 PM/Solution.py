// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        record = []
        
        def visit(node: 'Node', level: int):
            if node == None:
                return
            
            if len(record) < level:
                record.append(node)
            elif record[level-1] != node:
                record[level-1].next = node
                record[level-1] = node
            
            visit(node.left, level + 1)
            visit(node.right, level + 1)
            
            return
        
        visit(root, 1)
        
        return root