// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # --- plain two pass code: ---
#         curr = head
#         sz = 0
#         while(curr != None):
#             sz += 1
#             curr = curr.next
#         step = sz - n
        
#         if step is 0:
#             return head.next
        
#         tar = head
#         while(step>1):
#             tar = tar.next
#             step -= 1
#         tar.next = tar.next.next
#         return head
        
#         # store list in an array to find the one to delete next
#         a = []
#         curr = head
#         while(curr != None):
#             a.append(curr)
#             curr = curr.next
#         # print(a)
        
#         step = len(a) - n
        
#         if step is 0:
#             return head.next
        
#         tar = a[step-1]
#         # print(tar)
#         tar.next = tar.next.next
#         return head

        # two pointer solution
        hare = head
        for _ in range(n):
            hare = hare.next
        
        toi = head
        if hare == None:
            return head.next
        while(hare.next != None):
            toi = toi.next
            hare = hare.next
        
        toi.next = toi.next.next
        return head
        
        
        