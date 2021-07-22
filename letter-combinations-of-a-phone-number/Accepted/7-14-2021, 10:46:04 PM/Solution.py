// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ""
        dic = {
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w", "x", "y", "z"]
        }
        
        res = []
        self.curr = []
        
        def backtrack(ind: int):
            # build starting at index
            if ind == len(digits):
                res.append("".join(self.curr))
                return
            
            for c in dic[digits[ind]]:
                self.curr.append(c)
                backtrack(ind + 1)
                self.curr.pop()
                
        backtrack(0)
        return res
            
        