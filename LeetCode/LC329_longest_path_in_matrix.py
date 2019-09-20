class Solution:
    def __init__(self, *args, **kwargs):
        self.dirs = [
            [0, 1], [1, 0], [0, -1], [-1, 0]
        ]
        self.m = None
        self.n = None

    def longestIncreasingPath(self, matrix: 'List[List[int]]') -> int:
        if len(matrix) == 0:
            return 0
        self.m = len(matrix)
        self.n = len(matrix[0])

        ans = 0

        for i in range(self.m):
            for j in range(self.n):
                ans = max(ans, self.dfs(matrix, i, j))
        return ans

    def dfs(self, matrix, i, j):
        ans = 0
        for d in self.dirs:
            x = i + d[0]
            y = j + d[1]
            if x >= 0 and x < self.m and y >= 0 and y < self.n and matrix[x][y] > matrix[i][j]:
                ans = max(ans, self.dfs(matrix, x, y))
        ans += 1
        return ans


nums = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]

print(Solution().longestIncreasingPath(nums))
