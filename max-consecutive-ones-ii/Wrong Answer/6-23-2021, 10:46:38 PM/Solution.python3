// https://leetcode.com/problems/max-consecutive-ones-ii

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        in_stream = False
        # are we currently in a "1" stream
        curr_stream = 0
        # length of the current "1" stream
        res = 0
        # best result till now
        last_stream = 0
        # length of last "1" stream separated by at most 1 "0"
        
        if nums[0] == 1:
            in_stream = True
            curr_stream = 1
            res = 1
            
        for i in range(1, len(nums)):
            # print(in_stream)
            # print(curr_stream)
            # print(last_stream)
            if in_stream:
                if nums[i] == 0:
                    in_stream = False
                    last_stream = curr_stream
                    curr_stream = 0
                else:
                    curr_stream += 1
                    res = max(res, curr_stream + last_stream + 1)
            else:
                if nums[i] == 0:
                    last_stream = 0
                else:
                    in_stream = True
                    curr_stream = 1
                    res = max(res, curr_stream + last_stream + 1)
        
        return res
                    
                    
                    
                    