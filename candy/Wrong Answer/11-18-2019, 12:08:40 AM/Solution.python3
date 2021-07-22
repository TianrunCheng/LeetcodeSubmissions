// https://leetcode.com/problems/candy

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 0:
            return 1
        i = 0
        candies = 0
        
        block_len = 0
        block_candies = 0
        block_ending = 0
        block_start = 0
        
        curr_candies = 0
        
        stack = [-1]
        
        while i < len(ratings):
            if stack[-1] == -1:
                stack.append(ratings[i])
                candies += block_candies
                block_len = 1
                curr_candies = 1
                block_candies = 1
                block_start = 1
            else:
                if stack[-1] < ratings[i]:  # going up in block
                    curr_candies += 1
                    block_len += 1
                    block_candies += curr_candies
                    stack.append(ratings[i])
                elif stack[-1] > ratings[i]:  # going down
                    if len(stack) > 2 and stack[-2] < stack[-1]:  # going down and make block
                        
                        candies += block_candies
                        candies = candies - min(block_start, block_ending)
                        stack = [-1, stack[-1]]
                        block_ending = curr_candies
                        
                        stack.append(ratings[i])
                        block_len = 2
                        block_candies = 3
                        curr_candies = 1
                        block_start = 2
                    else:  # going down in same block
                        if curr_candies > 1:
                            curr_candies = curr_candies - 1
                            block_len += 1
                            block_candies += curr_candies
                            stack.append(ratings[i])
                        else:  # rising the ground of block by 1
                            block_len += 1
                            block_candies += block_len
                            block_start += 1
                elif stack[-1] == ratings[i]:
                    candies += block_candies
                    candies = candies - min(block_start, block_ending)
                    stack = [-1]
                    block_ending = 0
                    
                    stack.append(ratings[i])
                    block_len = 1
                    block_candies = 1
                    curr_candies = 1
                    block_start = 1
            i += 1
        candies += block_candies
        candies = candies - min(block_start, block_ending)
        return candies
                        
                        