// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.curr = []
        used = set()
        
        res = []
        
        def backtrack():
            if len(self.curr) == len(nums):
                # print(self.curr)
                res.append(self.curr.copy())
                # cannot append (self.curr), will not create new copy of curr
                return
            
            for num in nums:
                if num not in used:
                    self.curr.append(num)
                    used.add(num)
                    backtrack()
                    used.remove(num)
                    self.curr.pop()
        
        backtrack()
        
        return res