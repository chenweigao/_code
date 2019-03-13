def uniquePathsIII(self, A):
    self.res = 0
    m, n, empty = len(A), len(A[0]), 1
    for i in range(m):
        for j in range(n):
            if A[i][j] == 1:
                x, y = (i, j)
            elif A[i][j] == 2:
                end = (i, j)
            elif A[i][j] == 0:
                empty += 1

    def dfs(x, y, empty):
        if not (0 <= x < m and 0 <= y < n and A[x][y] >= 0):
            return
        if (x, y) == end:
            if empty == 0:
                self.res += 1
            return
        A[x][y] = -2
        dfs(x + 1, y, empty - 1)
        dfs(x - 1, y, empty - 1)
        dfs(x, y + 1, empty - 1)
        dfs(x, y - 1, empty - 1)
        A[x][y] = 0
    dfs(x, y, empty)
    return self.res


'''
算法思路：
1. 先统计给定数组中的数组，确定起点、终点和可以访问的个数
2. 暴力dfs, 分情况讨论：
    - x, y 不满足条件，直接 return
    - 数组值不为 0, 不可访问，直接 return
    - 如果遇到终点并且数组中没有被访问的元素，res++
3. 讲当前的 x, y 标记为 -2, 表示已访问
4. 暴力 dfs 可能的四个点
5. 将路线和标记恢复成上一次的状态
6. 返回 res
'''