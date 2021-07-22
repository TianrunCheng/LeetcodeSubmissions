// https://leetcode.com/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # process from the right end
        # information we need to determine arr[i] have seen
        # record it in a stack
        # a "76" earlier than "73" will make the latter never seen by days before
        stack = []
        # record the meaningful seen temps and its day-number
        # saves time because possible vals for temps is far smaller than len(temps)
        n = len(temperatures)
        res = [0] * n
        
        for i in range(n-1, -1, -1):
            curr = temperatures[i]
            while(len(stack) > 0):
                if stack[-1][0] <= curr:
                    stack.pop()
                else:
                    break
            if len(stack) > 0:
                days = stack[-1][1] - i
                res[i] = days
            stack.append((curr, i))
            
        return res