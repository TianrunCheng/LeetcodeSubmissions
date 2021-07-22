// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        res = dummy
        one = False
        # whether there's an 1 adding to this digit
        while l1 or l2:
            curr = 0
            if l1:
                curr += l1.val
                l1 = l1.next
            if l2:
                curr += l2.val
                l2 = l2.next
            if one:
                curr += 1
            # curr is the value supposed to be stored in this node
            if curr > 9:
                one = True
                curr = curr % 10
                res.next = ListNode(curr)
                res = res.next
            else:
                one = False
                res.next = ListNode(curr)
                res = res.next
        if one:
            res.next = ListNode(1)
            
        return dummy.next
            