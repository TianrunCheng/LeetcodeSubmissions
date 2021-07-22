// https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        
        size = 1
        curr = head
        while curr.next:
            size += 1
            curr = curr.next
        # curr -> none 
        # curr is the tail now
        tail = curr
        tail.next = head
        
        k = k % size
        for _ in range(size - k):
            tail = tail.next
            head = head.next
        tail.next = None
        return head