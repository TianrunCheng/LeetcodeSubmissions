// https://leetcode.com/problems/most-common-word

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        para = paragraph.split()
        ban_dic = {}
        for _ in banned:
            ban_dic[_] = 0
        
        term_dic = {}
        for _ in para:
            _ = _.lower()
            _ = _.strip(',.')
            if _ not in ban_dic:
                if _ not in term_dic:
                    term_dic[_] = 1
                else:
                    term_dic[_] += 1
        
        print(term_dic)
        freq = []
        for _ in term_dic:
            freq.append(term_dic[_])
        
        freq.sort()
        
        for _ in term_dic:
            if term_dic[_] == freq[-1]:
                return _