// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        
        result = []
        if len(digits) is 0:
            return result
        
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
        
        def build_string():
            curr_string = ""
            for j in range(n):
                curr_string += dic[digits[j]][state[j]]
            return curr_string
        
        n = len(digits)
        state = [0 for i in range(n)]
        result.append(build_string())
        # which letter we're at for each digit
        while True:
            flag = False
            for i in reversed(range(n)):
                if state[i] < len(dic[digits[i]])-1:
                    state[i] += 1
                    if i is not (n-1):
                        for j in range(i+1, n):
                            state[j] = 0
                    result.append(build_string())
                    flag = True
                    break
            if not flag:
                break
        
        return result