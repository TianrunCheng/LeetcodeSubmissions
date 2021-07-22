// https://leetcode.com/problems/the-skyline-problem

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        def mergeSkylines(x: List[List[int]], y: List[List[int]]):
            # print(x)
            # print(y)
            res = []
            hx = 0; hy = 0; h = 0
            i = 0; j = 0
            while i < len(x) and j < len(y):
                if x[i][0] < y[j][0]:
                    # next changing skyline is x
                    hx = x[i][1]
                    if h != max(hy, hx):
                        h = max(hy, hx)
                        res.append([x[i][0], h])
                    i += 1
                elif y[j][0] < x[i][0]:
                    # next changing skyline is y
                    hy = y[j][1]
                    if h != max(hy, hx):
                        h = max(hy, hx)
                        res.append([y[j][0], h])
                    j += 1
                else:
                    # x and y skylines changed at the same time
                    hx = x[i][1]; hy = y[j][1]
                    if h != max(hy, hx):
                        h = max(hy, hx)
                        res.append([y[j][0], h])
                    i += 1; j += 1
            if i == len(x):
                res.extend(y[j:])
            else:
                res.extend(x[i:])
            # print(res)
            # print()
            return res
        
        def recur(start: int, end: int) -> List[List[int]]:
            # build skyline of buildings[start: end+1]
            if start > end:
                return []
            if start == end:
                return [[buildings[start][0], buildings[start][2]], [buildings[start][1], 0]]
            mid = (start + end) // 2
            x = recur(start, mid)
            y = recur(mid+1, end)
            return mergeSkylines(x, y)
        
        return recur(0, len(buildings)-1)
                    