// https://leetcode.com/problems/implement-stack-using-queues

from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__queue = deque()
        self.__size = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.__queue.append(x)
        self.__size += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return -1
        for i in range(self.__size - 1):
            temp = self.__queue.popleft()
            self.__queue.append(temp)
        self.__size -= 1
        return self.__queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return -1
        for i in range(self.__size):
            temp = self.__queue.popleft()
            self.__queue.append(temp)
        return temp

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.__size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()