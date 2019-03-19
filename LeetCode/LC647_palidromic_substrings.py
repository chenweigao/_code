class Solution:
    def isPalindromic(self, s):
        if s == s[::-1]:
            return True
        return False

    def getAllSubstring(self, s):
        length = len(s)
        # for i in range(length):
        #     for j in range(i, length):
        # yield (s[i:j])
        return [s[i:j + 1] for i in range(length) for j in range(i, length)]

    def countSubstrings(self, s: str) -> int:
        res = []
        for sub in self.getAllSubstring(s):
            if self.isPalindromic(sub):
                res.append(sub)
        return len(res)


class Solution2:
    def countSubstrings(self, s):
        n = len(s)
        res = 0
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1])
                if dp[i][j]:
                    res += 1
        return res

    def getAllSubstring(self, s):
        length = len(s)
        for i in range(length):
            for j in range(i + 1, length + 1):
                yield(s[i:j])

        

s = 'abba'
print(Solution().getAllSubstring(s))
print(Solution2().countSubstrings(s))
print([_ for _ in Solution2().getAllSubstring(s)])