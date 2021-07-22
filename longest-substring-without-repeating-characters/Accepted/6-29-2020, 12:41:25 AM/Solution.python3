// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # total number of substrings possible: n^2, checking if a substring has repeating chars: n
        # simple enumeration gives O(n^3) algorithm
        # how can we make it faster?
        # each position as a staring point for substring has its unique longest-sub-without-repeat
        
        # or is it an O(n) problem cause the biggest possible substring cannot exceed the number of chars?

# '''First successful submission, speed 6%'''
#         n = len(s) 
#         l = 1 # current longest 
#         if len(s) == 0:
#             return 0
#                     # 'a':0,
#                     # 'b':0,
#                     # 'c':0,
#                     #  ...
#                     # 'z':0
        
#         for c in range(len(s)):
#             if (n-c) <= l:
#                 return l
#             else:
#                 Dict={}
#                 Dict[s[c]] = 1
#                 curr_l = 1
#                 for i in range(c+1, n):
#                     if s[i] not in Dict:
#                         Dict[s[i]] = 1
#                         curr_l = i-c+1
#                         l = max(curr_l, l)
#                     else:
#                         print(curr_l)
#                         l = max(curr_l, l)
#                         break
        
#         return l
                    
        n = len(s) 
        l = 1 # current longest 
        if len(s) == 0:
            return 0
                    # 'a':0,
                    # 'b':0,
                    # 'c':0,
                    #  ...
                    # 'z':0
        
        for c in range(len(s)):
            if (n-c) <= l:
                return l
            else:
                fSet = set()
                fSet.add(s[c])
                curr_l = 1
                for i in range(c+1, n):
                    if s[i] not in fSet:
                        fSet.add(s[i])
                        curr_l = i-c+1
                        l = max(curr_l, l)
                    else:
                        print(curr_l)
                        l = max(curr_l, l)
                        break
        
        return l