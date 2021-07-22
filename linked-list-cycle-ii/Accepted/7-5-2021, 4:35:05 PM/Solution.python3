// https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        slow = head
        fast = head
        cycle = False
        
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                intersect = slow
                cycle = True
                break
        
        if not cycle:
            return None
        
        fast = head
        slow = intersect
        while(fast != slow):
            fast = fast.next
            slow = slow.next
            
        return slow