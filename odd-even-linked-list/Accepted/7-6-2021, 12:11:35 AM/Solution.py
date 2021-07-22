// https://leetcode.com/problems/odd-even-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if head == None or head.next == None:
            return head
        
        dummy = ListNode()
        even = dummy
        curr = head
        
        while curr.next:
            print(curr.val)
            even.next = curr.next
            even = even.next
            if curr.next.next:
                curr.next = curr.next.next
                curr = curr.next
            else:
                break
                
        even.next = None
        # remember to trim the last node after done connecting!
        curr.next = dummy.next
        
        return head

            