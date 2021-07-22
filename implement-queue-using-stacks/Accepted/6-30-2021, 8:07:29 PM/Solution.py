// https://leetcode.com/problems/implement-queue-using-stacks

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__store = []
        self.__cache = []
        self.__size = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.__store.append(x)
        self.__size += 1
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return -1
        if len(self.__cache) > 0:
            self.__size -= 1
            return self.__cache.pop()
        else:
            for i in range(self.__size):
                temp = self.__store.pop()
                self.__cache.append(temp)
            self.__store = []
            self.__size -= 1
            return self.__cache.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return -1
        if len(self.__cache) > 0:
            return self.__cache[-1]
        else:
            for i in range(self.__size):
                temp = self.__store.pop()
                self.__cache.append(temp)
            self.__store = []
            return self.__cache[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.__size == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()