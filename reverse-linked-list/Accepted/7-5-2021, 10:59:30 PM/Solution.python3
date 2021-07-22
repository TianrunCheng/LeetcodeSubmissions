// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev_node = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next # Remember next node
            curr_node.next = prev_node  # REVERSE! None, first time round.
            prev_node = curr_node  # Used in the next iteration.
            curr_node = next_node  # Move to next node.
        head = prev_node
        return head

        
#         # recursive: O(n^2)
#         if head == None or head.next == None:
#             return head
        
#         curr = self.reverseList(head.next)
        
#         head.next.next = head
#         head.next = None
        
#         return curr
        
        
        
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