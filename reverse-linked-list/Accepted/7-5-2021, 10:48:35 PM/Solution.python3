// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        curr = head
        # exclude the first element, recursively solve start from head.next
        head = self.reverseList(head.next)
        tail = head
        while(tail.next != None):
            tail = tail.next
        tail.next = curr
        curr.next = None
        return head
        
#         if head == None:
#             return None
        
#         tail = head
#         while(tail.next != None):
#             curr = tail.next
#             tail.next = tail.next.next
#             curr.next = head
#             head = curr
        
#         return head