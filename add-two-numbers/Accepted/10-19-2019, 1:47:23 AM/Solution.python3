// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = 0
        n2 = 0
        i = 1
        while l1 != None:
            n1 += i * l1.val
            i = i * 10
            l1 = l1.next
        i = 1
        while l2 != None:
            n2 += i * l2.val
            i = i * 10
            l2 = l2.next
        an = n1 + n2
        ans = str(an)
        lb = None
        for _ in ans:
            la = ListNode(int(_))
            la.next = lb
            lb = la
        return la