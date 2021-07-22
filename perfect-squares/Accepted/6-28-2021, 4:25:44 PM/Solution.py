// https://leetcode.com/problems/perfect-squares

from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        # construct a list of all perfect squares smaller than n
        squares = []
        queue = deque()
        # queue of all reachable numbers with "step" adding of squares
        seen = set()
        # all seen numbers
        for i in range(1, n+1):
            sq = i * i
            if sq <= n:
                squares.append(sq)
                queue.append(sq)
                seen.add(sq)
            else:
                break
        
        step = 0
        while(True):
            step += 1
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if curr == n:
                    return step
                for sq in squares:
                    p = curr + sq
                    if p not in seen:
                        seen.add(p)
                        queue.append(p)
        
                