// https://leetcode.com/problems/copy-list-with-random-pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        dic = {}
        # store the corresponding copy of each original node
        # dic[original_node] = copy_node
        dummy = Node(0)
        ptr = dummy
        curr = head
        while curr:
            p = Node(curr.val)
            dic[curr] = p
            ptr.next = p
            ptr = ptr.next
            curr = curr.next
        # dummy -> copied list
        
        curr = head
        ptr = dummy.next
        while curr:
            rand = curr.random
            if rand:
                ptr.random = dic[rand]
            curr = curr.next
            ptr = ptr.next
        
        return dummy.next