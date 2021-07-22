// https://leetcode.com/problems/the-skyline-problem

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
            edge = []
            hdict = collections.defaultdict(int)
            maxheap = []

            for s, e, h in buildings:
                edge.append((s, -1, h))
                edge.append((e, 1, h))
            edge.sort()
            #print edge
            ans = []
            for x, t, h in edge:
                if t == -1:
                    heapq.heappush(maxheap, -h)
                    hdict[h] += 1
                    while hdict[-maxheap[0]] == 0:
                        heapq.heappop(maxheap)
                    curH = -maxheap[0]
                    if curH == h and hdict[h] == 1:
                        point = [x, h]
                        if ans and ans[-1][0] == x:
                            point = max(point, ans.pop())
                        ans.append(point)
                else:
                    hdict[h] -= 1
                    while maxheap and hdict[-maxheap[0]] == 0:
                        heapq.heappop(maxheap)
                    curH = -maxheap[0] if maxheap else 0
                    if curH < h:
                        ans.append([x, curH])
            return ans
        