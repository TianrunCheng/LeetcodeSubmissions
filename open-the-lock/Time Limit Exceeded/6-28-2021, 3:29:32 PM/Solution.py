// https://leetcode.com/problems/open-the-lock

from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # each step we could turn one wheel one slot
        # 4 wheels * 2 directions = 8 possible next steps
        # bredth first search? 
        #   reaching target: return steps; 
        #   reaching deadend: don't use it to add to queue of (step+1)'s starting point
        # complexity of this method?
        
        for pos in deadends:
            if pos == target:
                return -1
        
        def turnLock(curr: str) -> list:
            curr = list(curr)
            res = []
            for i in range(4):
                num = int(curr[i])
                turnForward = (num + 1) % 10
                curr[i] = str(turnForward)
                res.append("".join(curr))
                turnBackward = (num - 1) % 10
                curr[i] = str(turnBackward)
                res.append("".join(curr))
                curr[i] = str(num)
            # print(res)
            return res
                
        queue = deque()
        queue.append("0000")
        step = 0
        seen = set()
        # queue includes the possible lock state at step
        while(len(queue) > 0):
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if curr not in seen:
                    seen.add(curr)
                    if curr == target:
                        return step
                    if curr not in deadends:
                        res = turnLock(curr)
                        for turn in res:
                            if turn not in queue:
                                queue.append(turn)
            step += 1
        
        return -1