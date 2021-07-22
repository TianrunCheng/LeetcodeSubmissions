// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        availability_stats = {}
        chars_len = len(chars)
        for c in chars:
            if c not in availability_stats:
                availability_stats[c] = 0
            else:
                availability_stats[c] += 1
        
        sum_of_len = 0
        
        
        for word in words:
            if len(word) > chars_len:
                continue  
            remaining_availability = availability_stats.copy()
            flag_good = True
            for w in word:
                if w in remaining_availability:
                    if remaining_availability[w] > 1:
                        remaining_availability[w] -= 1
                    else:
                        del remaining_availability[w]
                else:
                    flag_good = False
                    break
            if flag_good:
                sum_of_len += len(word)
            
        return sum_of_len
                    