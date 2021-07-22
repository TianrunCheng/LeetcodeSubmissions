// https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__data = []
        

    def push(self, val: int) -> None:
        self.__data.append(val)

    def pop(self) -> None:
        self.__data.pop()

    def top(self) -> int:
        return self.__data[-1]

    def getMin(self) -> int:
        res = self.__data[0]
        for num in self.__data:
            if num < res:
                res = num
        return res
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()