// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = ListNode()
        head = dummy
        while(l1 != None or l2 != None):
            if l1 == None:
                head.next = l2
                head = head.next
                l2 = l2.next
            elif l2 == None:
                head.next = l1
                head = head.next
                l1 = l1.next
            else:
                if l1.val > l2.val:
                    head.next = l2
                    head = head.next
                    l2 = l2.next
                else:
                    head.next = l1
                    head = head.next
                    l1 = l1.next
        return dummy.next