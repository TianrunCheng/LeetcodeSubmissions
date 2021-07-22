// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head == None:
            return head
        
        curr = head
        
        def recur(head: 'Node') -> 'Node':
            # flatten double link list starting from head
            # return tail of flattened list
            curr = head
            while curr.next or curr.child:
                if curr.child:
                    tail = recur(curr.child)
                    # weave curr.child - ... - tail after curr into list
                    if curr.next:
                        curr.next.prev = tail
                    tail.next = curr.next
                    curr.next = curr.child
                    curr.child.prev = curr
                    curr.child = None
                    curr = tail
                if curr.next:
                    curr = curr.next
            return curr
        
        recur(curr)
        
        return head