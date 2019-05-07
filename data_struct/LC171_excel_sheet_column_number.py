class Solution:
    def titleToNumber(self, s: str) -> int:
        s = s[::-1]
        res = 0

        for exp, ch in enumerate(s):
            res += (ord(ch) - 65 + 1) * (26 ** exp)

        return res


print(Solution().titleToNumber('ZY'))
