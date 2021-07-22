// https://leetcode.com/problems/intersection-of-two-linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pointA = headA
        pointB = headB
        lengthA = 0
        lengthB = 0
        while(pointA != None):
            lengthA += 1
            pointA = pointA.next
        while(pointB != None):
            lengthB += 1
            pointB = pointB.next
        
        if lengthB < lengthA:
            pointA = headB
            pointB = headA
            delta = lengthA - lengthB
        else:
            pointA = headA
            pointB = headB
            delta = lengthB - lengthA
        
        for i in range(delta):
            print(pointB.val)
            pointB = pointB.next
        
        while True:
            if pointA == pointB:
                return pointA
            if pointA == None:
                return None
            pointA = pointA.next
            pointB = pointB.next
        
        
        
        
        
        
        