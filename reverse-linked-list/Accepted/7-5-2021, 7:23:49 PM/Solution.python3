// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        tail = head
        while(tail.next != None):
            curr = tail.next
            tail.next = tail.next.next
            curr.next = head
            head = curr
        
        return head