// https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        dic = {}
        # {
        #   key: value
        # }
        # key: char; value: num of appearance in t
        for c in t:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        
        # print(dic)
        

        left = 0
        right = 0
        s = list(s)
        # current_substring = s[left, right]
        # current_substring=""
        # current_dic={}
        hit_dic = {}
        # if s[0] in dic:
        #     hit_dic[s[0]] = 1
        # if t == s[0]:
        #     return s[0]
        
        flag = False
        min_length = m
        res = ""
        # current_length=n
        # optimal_substring=""
        
        while( right < m ):
            # print("left: " + str(left) + "  right: " + str(right))
            # print(flag)
            # print(hit_dic)

            if not flag:  # s[left, right] doesn't include t, growing phase
                curr = s[right]
                if curr in dic:
                    if curr not in hit_dic:
                        hit_dic[curr] = 1
                    else:
                        hit_dic[curr] += 1
                    state = True
                    for c in dic:
                        if c not in hit_dic:
                            state = False
                            break
                        elif hit_dic[c] < dic[c]:
                            state = False
                            break
                    if state:
                        flag = True
                    else:
                        right += 1

                else:
                    right += 1

            else:
                # s[left, right] includes t, dwindling phase
                curr = s[left]
                # print(curr)
                if curr in dic:
                    if hit_dic[curr] > dic[curr]:
                        # print(hit_dic)
                        # can afford to exclude this curr char
                        hit_dic[curr] -= 1
                        left += 1
                    else:
                        # s[left, right] is a local minWindow
                        if (right - left + 1) < min_length:
                            res = "".join(s[left:right+1])
                            # print(res)
                            min_length = right - left
                        left += 1
                        if hit_dic[curr] > 1:
                            hit_dic[curr] -= 1
                        else:
                            del hit_dic[curr]
                        flag = False
                        right += 1
                else:
                    left += 1
            
        return res
                
        
        

        # while(left < (n+1)):
        #     while(right < (n+1)):
        #         current_c=s[right]
        #         current_substring = current_substring + current_c
        #         if dic[current_c] >= 1:
        #             if current_c not in current_dic:
        #                 current_dic[current_c]=1
        #             else:
        #                 current_dic[current_c]+=1
        #         if current_dic == dic:
        #             current_length = len(current_substring)
        #         if current_length< min_length:
        #             min_length=current_length
        #             optimal_substring=current_substring
        #         right += 1
            
                        
            
                
          
        
        
        return ""