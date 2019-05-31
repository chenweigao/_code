class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        # 10 ^ 6 = 2 ^ 10 * 2 ^ 10 = 2 ^ 20
        prime = [2, 3, 5, 7, 11, 13, 17, 19]
        res = 0

        for i in range(L, R + 1):
            tmp = self.numberOfOneBits(i)
            if tmp in prime:
                res += 1
        return res

    def numberOfOneBits(self, n):
        count = 0
        while n != 0:
            n &= (n - 1)
            count += 1
        return count


L = 567
R = 607
print(Solution().countPrimeSetBits(L, R))
