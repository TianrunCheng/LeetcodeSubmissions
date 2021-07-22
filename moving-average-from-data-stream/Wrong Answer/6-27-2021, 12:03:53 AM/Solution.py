// https://leetcode.com/problems/moving-average-from-data-stream

from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.__q = deque(maxlen = 3)

    def next(self, val: int) -> float:
        self.__q.append(val)
        mean = 0
        for ele in self.__q:
            mean += ele
        return mean / 3


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)