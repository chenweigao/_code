import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = collections.Counter(s)
        res = 0
        print(dic)
        for k, v in dic.items():
            res += v // 2 * 2
            if res % 2 == 0 and v % 2 == 1:
                res += 1
        return res


s = "abccccdd"
print(Solution().longestPalindrome(s))
