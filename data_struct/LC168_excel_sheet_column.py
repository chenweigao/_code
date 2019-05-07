class Solution:
    def convertToTitle(self, n: int) -> str:
        dic = {}
        for i in range(26):
            dic[i] = chr(i + 65) # ord('A') = 65
        res = ''
        while n:
            res = dic[(n - 1) % 26] + res
            n = (n - 1) // 26
        return res

class Solution2:
    def convertToTitle(self, n: int) -> str:
        res = ''

        while n:
            n -= 1
            res = chr(n % 26 + ord('A')) + res
            n //= 26
        return res

print(Solution().convertToTitle(701))