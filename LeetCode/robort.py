def uniquePath(m, n):
    dp = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]
    
print(uniquePath(7, 3))

