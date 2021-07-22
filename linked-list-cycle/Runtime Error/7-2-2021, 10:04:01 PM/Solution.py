// https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        fast = head.next
        slow = head
        
        while(True):
            if not fast:
                return False
            elif fast == slow:
                return True
            fast = fast.next
            if fast.next != None:
                fast = fast.next
            else:
                return False
            slow = slow.next