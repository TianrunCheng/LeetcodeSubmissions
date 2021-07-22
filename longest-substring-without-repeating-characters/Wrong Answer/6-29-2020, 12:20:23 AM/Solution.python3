// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # total number of substrings possible: n^2, checking if a substring has repeating chars: n
        # simple enumeration gives O(n^3) algorithm
        # how can we make it faster?
        # each position as a staring point for substring has its unique longest-sub-without-repeat
        
        # or is it an O(n) problem cause the biggest possible substring cannot exceed the number of chars?
        n = len(s) 
        l = 0 # current longest 
        # if len(s) == 0:
        #     return 0
                    # 'a':0,
                    # 'b':0,
                    # 'c':0,
                    # 'd':0,
                    # 'e':0,
                    # 'f':0,
                    # 'g':0,
                    # 'h':0,
                    # 'i':0,
                    # 'j':0,
                    # 'k':0,
                    # 'l':0,
                    # 'm':0,
                    # 'n':0,
                    # 'o':0,
                    # 'p':0,
                    # 'q':0,
                    # 'r':0,
                    # 's':0,
                    # 't':0,
                    # 'u':0,
                    # 'v':0,
                    # 'w':0,
                    # 'x':0,
                    # 'y':0,
                    # 'z':0
        
        for c in range(len(s)):
            if (n-c) <= l:
                return l
            else:
                Dict = {}
                Dict[s[c]] = 1
                curr_l = 1
                for i in range(c+1, n):
                    if s[i] not in Dict:
                        Dict[s[i]] = 1
                        curr_l = i-c+1
                    else:
                        print(curr_l)
                        l = max(curr_l, l)
                        break
        
        return l
                    
        