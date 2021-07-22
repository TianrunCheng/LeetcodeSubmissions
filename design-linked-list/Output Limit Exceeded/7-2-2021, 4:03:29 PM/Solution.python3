// https://leetcode.com/problems/design-linked-list

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0

    def printList(self) -> None:
        print("print linked list:")
        res = []
        curr = self.head
        while curr != None:
            res.append(" -> " + str(curr.val))
            curr = curr.next
        print("".join(res))
    
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        print("get " + str(index))
        self.printList()
        if index < 0 or index >= self.length:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        print("add at head " + str(val))
        self.printList()
        temp = Node(val)
        if self.head != None:
            temp.next = self.head
            self.head = temp
        else:
            self.head = temp
        self.length += 1
        self.printList()

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        print("add at tail " + str(val))
        self.printList()
        temp = Node(val)
        curr = self.head
        if curr:
            while(curr.next):
                curr = curr.next
            curr.next = temp
        else:
            self.head = temp
        self.length += 1
        self.printList()
            

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        print("add at index " + str([index, val]))
        self.printList()
        if index < 0:
            return
        if index == 0:
            self.addAtHead(val)
        if index > self.length:
            return
        if self.head:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            temp = Node(val)
            temp.next = curr.next
            curr.next = temp
            self.length += 1
        else:
            self.head = Node(val)
            self.length += 1
        self.printList()
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        print("delete at index " + str(index))
        self.printList()
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
        elif 0 < index < self.length:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
            self.length -= 1
        self.printList()
                
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)