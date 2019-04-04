class Solution:
    def longestPalindrome(self, s):
        res = ''
        for i in range(len(s)):
            # tmp = self.helper(s, i, i)
            # if len(tmp) > len(res):
            #     res = tmp
            # tmp = self.helper(s, i, i + 1)
            # if len(tmp) > len(res):
            #     res = tmp

            # len1 = self.helper(s, i, i) 奇数情况
            # len2 = self.helper(s, i, i + 1) 偶数情况
            res = max(self.helper(s, i, i), self.helper(
                s, i, i + 1), res, key=len)

        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r] # 注意这里是切片，所以是半开半闭区间


print(Solution().longestPalindrome('cabbaad'))
