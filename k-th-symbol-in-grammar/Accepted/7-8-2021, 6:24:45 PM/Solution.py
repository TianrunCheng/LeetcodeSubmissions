// https://leetcode.com/problems/k-th-symbol-in-grammar

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def rec(n: int, k: int) -> int:
            # return row n ind k element
            if n == 1:
                return 0
            if k % 2 == 1:
                return rec(n - 1, k // 2 + 1)
            else:
                return xor(n - 1, k // 2)
        
        def xor(n: int, k: int) -> int:
            # return xor of row n ind k element
            if n == 1:
                return 1
            if k % 2 == 1:
                return xor(n - 1, k // 2 + 1)
            else:
                return rec(n - 1, k // 2)
            
        return rec(n, k)