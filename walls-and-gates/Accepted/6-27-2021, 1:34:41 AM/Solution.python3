// https://leetcode.com/problems/walls-and-gates

from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        inf = 2 ** 31 - 1
        dq = deque()
        m = len(rooms)
        n = len(rooms[0])
        
        gates = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    gates.append((i, j))
        
        # print(gates)
        
        for gate in gates:
            i = gate[0]
            j = gate[1]
            step = 0
            dq.append((i, j))
            while(len(dq) > 0):
                # print(rooms)
                # print(dq)
                step += 1
                for i in range(len(dq)):
                    curr = dq.popleft()
                    i = curr[0]; j = curr[1]

                    if i > 0 and rooms[i-1][j] > step:
                        rooms[i-1][j] = step
                        dq.append((i-1, j))
                    if j > 0 and rooms[i][j-1] > step:
                        rooms[i][j-1] = step
                        dq.append((i, j-1))
                    if i < (m-1) and rooms[i+1][j] > step:
                        rooms[i+1][j] = step
                        dq.append((i+1, j))
                    if j < (n-1) and rooms[i][j+1] > step:
                        rooms[i][j+1] = step
                        dq.append((i, j+1))
        return