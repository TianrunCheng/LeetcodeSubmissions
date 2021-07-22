// https://leetcode.com/problems/unique-binary-search-trees

class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        res = [0] * (n+1)
        res[0] = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                res[i] += res[j-1] * res[i-j]
        # print(res)
        return res[n]