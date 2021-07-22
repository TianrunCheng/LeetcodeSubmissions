// https://leetcode.com/problems/design-circular-queue

class MyCircularQueue:

    def __init__(self, k: int):
        self.__queue = [0] * k
        self.__len = k
        self.__head = -1
        self.__tail = -1

    def enQueue(self, value: int) -> bool:
        if self.__head == -1:
            self.__queue[0] = value
            self.__head += 1
            self.__tail += 1
            # print(self.__queue)
            return True
        if self.__head == (self.__tail + 1) % self.__len:
            # print(self.__queue)
            return False
        self.__tail = (self.__tail + 1) % self.__len
        self.__queue[self.__tail] = value
        # print(self.__queue)
        return True

    def deQueue(self) -> bool:
        if self.__head == -1:
            # print(self.__queue)
            return False
        if self.__head == self.__tail:
            self.__head = -1
            self.__tail = -1
            # print(self.__queue)
            return True
        self.__head = (self.__head + 1) % self.__len
        # print(self.__queue)
        return True

    def Front(self) -> int:
        if self.__head == -1:
            # print(self.__queue)
            return -1
        # print(self.__queue)
        return self.__queue[self.__head]

    def Rear(self) -> int:
        if self.__head == -1:
            # print(self.__queue)
            return -1
        # print(self.__queue)
        return self.__queue[self.__tail]

    def isEmpty(self) -> bool:
        # print(self.__queue)
        return self.__head == -1

    def isFull(self) -> bool:
        # print(self.__queue)
        return self.__head == (self.__tail + 1) % self.__len


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()