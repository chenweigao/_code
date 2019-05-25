from builtins import input


class Solution:
    def solution(self, matrix):
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == '1':
                        dp[i][j] = min(dp[i - 1][j], dp[i][j-1],
                                       dp[i-1][j - 1]) + 1
                ans = max(ans, dp[i][j])
        return ans ** 2


while True:
    try:
        matrix = []
        rows = int(input())
        for i in range(rows):
            line = input()
            matrix.append(line)
        # print(matrix)
        # print(matrix, columns, rows)
        ans = Solution().solution(matrix)
        print(ans)
    except:
        break
