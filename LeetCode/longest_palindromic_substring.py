def longestPalindrome(s):
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    res = ''
    for i in range(len(s)):
        for j in range(len(s) - 1, -1, -1):
            dp[i][j] = s[i] == s[j] and (i - j <= 2 or dp(i + 1, j - 1))
            if dp[i][j] and (res == '' or j - i + 1 > len(res)):
                res = s[i:j+1]

    return res


print(longestPalindrome('babadaaaaa'))
