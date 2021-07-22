// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # recursive: O(n)
        if head == None or head.next == None:
            return head
        
        curr = self.reverseList(head.next)
        # the recursive function only changed after head.next
        # head.next is pointing to the tail of returned list right now
        
        head.next.next = head
        head.next = None
        
        return curr
        
        
        
#         # recursive: traversing the entire returned list to find
#         #  the last place to add the excepted node, O(n^2)
#         if head == None or head.next == None:
#             return head
#         curr = head
#         # exclude the first element, recursively solve start from head.next
#         head = self.reverseList(head.next)
#         tail = head
#         while(tail.next != None):
#             tail = tail.next
#         tail.next = curr
#         curr.next = None
#         # curr's next has not been changed in the recursive function!
#         # it's pointing to the tail of the returned list!
#         return head
        
    
#         if head == None:
#             return None
        
#         tail = head
#         while(tail.next != None):
#             curr = tail.next
#             tail.next = tail.next.next
#             curr.next = head
#             head = curr
        
#         return head