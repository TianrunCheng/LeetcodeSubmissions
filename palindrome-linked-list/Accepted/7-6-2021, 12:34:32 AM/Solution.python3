// https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # maybe we could reverse the second half of the list
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        hal = head
        for _ in range(count // 2):
            hal = hal.next
        
        curr_hal = hal
        while hal.next:
            temp = hal.next
            hal.next = hal.next.next
            temp.next = curr_hal
            curr_hal = temp
        
        while curr_hal:
            if head.val == curr_hal.val:
                head = head.next
                curr_hal = curr_hal.next
            else:
                return False
        
        return True
            