// https://leetcode.com/problems/validate-stack-sequences

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        n = len(pushed)
        if n == 0:
            return True
        
        stack = []
        stack.append(pushed[0])
        push_ind = 1
        pop_ind = 0
        
        while(push_ind <= n):
            if len(stack)>0 and stack[-1] == popped[pop_ind]:
                stack.pop()
                pop_ind += 1
                # print(stack)
                # print(push_ind)
                # print(pop_ind)
            elif push_ind < n:
                stack.append(pushed[push_ind])
                push_ind += 1
                # print(stack)
                # print(push_ind)
                # print(pop_ind)
            else:
                break
        
        if pop_ind == n:
            return True
        
        return False