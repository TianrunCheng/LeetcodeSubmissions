// https://leetcode.com/problems/decode-string

class Solution:
    def decodeString(self, s: str) -> str:
        
        s = list(s)
        
        def readNum(start: int) -> int:
            end = start
            while(s[end].isdigit()):
                end += 1
            return end
        # s[end] is not a digit
        
        res = []
        
        def recurBuild(start: int) -> int:
            # build the result from s[start], return start of the next pattern
            i = start
            while(i < len(s) and s[i] != "]"):
                # print(str(i) + ": " + s[i])
                if s[i].isalpha():
                    res.append(s[i])
                    i += 1
                elif s[i].isdigit():
                    end = readNum(i)
                    num = int("".join(s[i:end]))
                    # print("num = " + str(num))
                    for j in range(num):
                        i = recurBuild(end+1)
                    
            return (i+1)
        
        recurBuild(0)
        return "".join(res)
    
    
    
    