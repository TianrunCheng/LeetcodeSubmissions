// https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows is 1:
            return s
        
        ans_array = []
        
        # create numRows empty strings for storing each row's answer
        for i in range(numRows):
            ans_array.append([])
        
        ptr = 0
        curr_row = 0
        flag = True  
        # remembering if we are going down(true) or up(false) in rows
        while(ptr < len(s)):
            
            ans_array[curr_row].append(s[ptr])
            # print(ans_array)
            
            if flag:
                if curr_row < (numRows - 1):
                    curr_row += 1
                else:
                    flag = False
                    curr_row -= 1
            else:
                if curr_row > 0:
                    curr_row -= 1
                else:
                    flag = True
                    curr_row += 1
                
            ptr += 1
            
        ans = ''
        for a in ans_array:
            ans += ''.join(a)
        
        return ans