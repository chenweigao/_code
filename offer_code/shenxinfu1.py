class Solution:
    def solution(self, array):
        res = 0
        dp = [[0 for _ in range(len(array))] for i in range(len(array[0]))]
        dp[0][0] = 0
        count = 0
        for i in range(len(array)):
            for j in range(len(array[0])):
                if i < len(array) - 1 and array[i + 1][j] != '-' and array[i][j] != '-':
                    if int(array[i + 1][j]) >= int(array[i][j]) and int(dp[i + 1][j]) != 1:
                        dp[i + 1][j] = 1
                        count += 1
                if j < len(array[0]) - 1 and array[i][j + 1] != '-' and array[i][j] != '-':
                    if  int(array[i][j + 1]) >= int(array[i][j]) and int(dp[i][j + 1]) != 1:
                        count += 1
                        dp[i][j + 1] = 1
                if i >= 1 and array[i - 1][j] != '-' and array[i][j] != '-':
                    if int(array[i - 1][j]) >= int(array[i][j]) and int(dp[i - 1][j]) != 1:
                        count += 1
                        dp[i - 1][j] = 1
                if j >= 1 and array[i][j - 1] != '-' and array[i][j] != '-':
                    if int(array[i][j - 1]) >= int(array[i][j - 1]) and int(dp[i][j - 1]) != 1:
                        count += 1
                        dp[i][j - 1] = 1
        
        return count - 1


res = []
while True:
    line = input()
    if not line.strip():
        break
    res.append(line.split())

print(Solution().solution(res))


# array = [
#     [1, 2, 3],
#     ['-', '-', 4],
#     [7, 6, 5]
# ]
# print(Solution().solution(res))