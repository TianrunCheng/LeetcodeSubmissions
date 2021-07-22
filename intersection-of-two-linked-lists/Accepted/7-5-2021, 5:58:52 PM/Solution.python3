// https://leetcode.com/problems/intersection-of-two-linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB
        
        while pA != pB:
            if pA == None:
                pA = headB
            else:
                pA = pA.next
            if pB== None:
                pB = headA
            else:
                pB = pB.next
        
        return pA
        
        
#         m = 0
#         ptr1 = headA
#         while ptr1 != None:
#             m += 1
#             ptr1 = ptr1.next
        
#         n = 0
#         ptr2 = headB
#         while ptr2 != None:
#             n += 1
#             ptr2 = ptr2.next
            
#         ptr1 = headA
#         ptr2 = headB
#         if m > n:
#             for _ in range(m - n):
#                 ptr1 = ptr1.next
#             while(ptr1 != None):
#                 if ptr1 == ptr2:
#                     return ptr1
#                 ptr1 = ptr1.next
#                 ptr2 = ptr2.next
#             return None
#         else:
#             for _ in range(n - m):
#                 ptr2 = ptr2.next
#             while(ptr1 != None):
#                 if ptr1 == ptr2:
#                     return ptr1
#                 ptr1 = ptr1.next
#                 ptr2 = ptr2.next
#             return None