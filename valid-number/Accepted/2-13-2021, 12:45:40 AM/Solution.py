// https://leetcode.com/problems/valid-number

class Solution:
    def isNumber(self, s: str) -> bool:
        
        digit_string = "0123456789"
        digit_list = list(digit_string)
        
        i = 0
        n = len(s)
        
        def readDigits(i: int):
            print("readDigits start " + str(i))
            start = i
            while(i<n and s[i] in digit_list):
                i += 1
            if i==start:
                print("readDigits -1")
                return -1
            print("readDigits end " + str(i-1))
            return (i-1)
        
        def readInteger(i: int):
            print("readInteger start " + str(i))
            start = i
            if i>= n:
                print("readInteger -1")
                return -1
            
            if s[i] is "+" or s[i] is "-":
                i += 1
            end = readDigits(i)
            print("readInteger end " + str(i))
            return end
        
        def readDecimalOrInt(i: int):
            print("readDecimal start " + str(i))
            if i>= n:
                print("readDecimal -1")
                return -1
            
            if s[i] is "+" or s[i] is "-":
                i += 1
                
            if s[i]==".":
                j = i + 1
                return readDigits(j)
            else:
                j = readDigits(i)
                if j < 0:
                    print("readDecimal -1")
                    return -1
                else:
                    sec = j + 1
                    if sec<n and s[sec] is ".":
                        sec_end = readDigits(sec+1)
                        if sec_end < 0:
                            print("readDecimal end " + str(i))
                            return sec
                        else:
                            print("readDecimal end " + str(i))
                            return sec_end
                    else:
                        print("readDecimal end " + str(i))
                        return (sec-1)
        
        dec = readDecimalOrInt(0)
        if dec < 0:
            return False
        if (dec+1) is n:
            return True
        print(s[dec+1])
        if s[dec+1].lower()=="e":
            order = readInteger(dec+2)
            if order<0:
                return False
            if order is (n-1):
                return True
            else:
                return False

        else:
            return False
            
        
        