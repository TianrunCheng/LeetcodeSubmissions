// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        ori = res
        while l1 != None or l2 != None:
            if l1 == None:
                res.next = l2
                res = res.next
                l2 = l2.next
            elif l2 == None:
                res.next = l1
                res = res.next
                l1 = l1.next
            elif l1.val <= l2.val:
                res.next = l1
                res = res.next
                l1 = l1.next
            else:
                res.next = l2
                res = res.next
                l2 = l2.next
        
        return ori.next