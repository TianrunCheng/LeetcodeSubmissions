// https://leetcode.com/problems/design-linked-list

class Node:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        # two dummy nodes, only to standardize work flow
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        if index < self.size // 2:
            curr = self.head
            for _ in range(index+1):
                curr = curr.next
            return curr.val
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
            return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.size += 1
        curr = Node(val)
        curr.next = self.head.next
        curr.prev = self.head
        self.head.next.prev = curr
        self.head.next = curr

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.size += 1
        curr = Node(val)
        curr.next = self.tail
        curr.prev = self.tail.prev
        self.tail.prev.next = curr
        self.tail.prev = curr
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return
        p = Node(val)
        if index < self.size // 2:
            # traverse from the front
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
            # add element before curr
            p.next = curr
            p.prev = curr.prev
            curr.prev.next = p
            curr.prev = p
            self.size += 1
        else:
            # traverse from the back
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
            # add before curr
            p.next = curr
            p.prev = curr.prev
            curr.prev.next = p
            curr.prev = p
            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        if index < self.size // 2:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
            # delete curr
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.size -= 1
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
            # delete curr
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)