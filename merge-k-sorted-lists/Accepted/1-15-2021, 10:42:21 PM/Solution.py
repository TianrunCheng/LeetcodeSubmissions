// https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        if len(lists) is 0:
            return None
        
        while(len(lists) > 1):
            merged_list = []
            
            for i in range(len(lists)//2):
                l1 = lists.pop()
                l2 = lists.pop()
                lm = ListNode()
                dummy = lm
                # print(dummy)
                # print(l1)
                # print(l2)
                while(l1 != None or l2 != None):
                    
                    if l2 is None:
                        lm.next = ListNode(l1.val)
                        lm = lm.next
                        l1 = l1.next
                    elif l1 is None:
                        lm.next = ListNode(l2.val)
                        lm = lm.next
                        l2 = l2.next
                    elif l1.val < l2.val:
                        lm.next = ListNode(l1.val)
                        lm = lm.next
                        l1 = l1.next
                    elif l2.val < l1.val:
                        lm.next = ListNode(l2.val)
                        lm = lm.next
                        l2 = l2.next
                    else:
                        lm.next = ListNode(l1.val)
                        lm = lm.next
                        lm.next = ListNode(l2.val)
                        lm = lm.next
                        l1 = l1.next
                        l2 = l2.next
                    
                merged_list.append(dummy.next)
                
            if len(lists)>0 :
                merged_list.append(lists.pop())
                
            lists = merged_list
        
        return lists[0]
                
                
                
                
                