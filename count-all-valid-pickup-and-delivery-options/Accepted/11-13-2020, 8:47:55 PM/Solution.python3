// https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options

class Solution:
    def countOrders(self, n: int) -> int:
        p = 10**9 + 7
        count = 1
        for i in range(n):
            count = count * (i + 1) * (2 * i + 1)
            # print(count)
            if count > p:
                count = count % p

        return count
            