// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        p = Node(insertVal)
        
        if not head:
            p.next = p
            return p
        
        start = head
        while(start.next.val >= start.val):
            # print(start.val)
            start = start.next
        # start.next is the min node
        
        if insertVal >= start.val or insertVal <= start.next.val:
            # add before the min node, after node start 
            # print(start.val)
            p.next = start.next
            start.next = p
        else:
            while(insertVal > start.next.val):
                # print(start.val)
                start = start.next
            # p <= start.next, add after start
            p.next = start.next
            start.next = p
        return head
            
        