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
        has_zero_before = False
        # does this stream of "1" has at least one "0" before it?
        
        if nums[0] == 1:
            in_stream = True
            curr_stream = 1
            res = 1
        else:
            has_zero_before = True
            
        for i in range(1, len(nums)):
            # print(in_stream)
            # print(curr_stream)
            # print(last_stream)
            if in_stream:
                # the last num is "1"
                if nums[i] == 0:
                    in_stream = False
                    last_stream = curr_stream
                    res = max(res, last_stream + 1)
                    # this "0" added to last stream is the longest valid sequence ending in the current index i
                    curr_stream = 0
                    has_zero_before = True
                else:
                    curr_stream += 1
                    if has_zero_before:
                        res = max(res, curr_stream + last_stream + 1)
                    else:
                        res = max(res, curr_stream)
            else:
                if nums[i] == 0:
                    last_stream = 0
                    
                else:
                    in_stream = True
                    curr_stream = 1
                    if has_zero_before:
                        res = max(res, curr_stream + last_stream + 1)
        
        res = max(res, 1)
        
        return res
                    
                    
                    
                    