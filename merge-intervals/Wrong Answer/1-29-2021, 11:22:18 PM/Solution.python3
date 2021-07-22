// https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key = lambda intervals: intervals[0])
        result = [intervals[0]]
        
        for interval in intervals:
            if interval[1] <= result[-1][1]:
                pass
            elif interval[0] <= result[-1][1]:
                result[-1][1] = interval[1]
            else:
                result.append(interval)
        
        return result