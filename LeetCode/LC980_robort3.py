


def dfs(x, y, empty):
    res = 0
    if not (0 <= x < m and 0 <= y < n and grid[x][y] >= 0):
        return
    if (x, y) == end:
        res += empty == 0  # why
        return
    grid[x][y] = -2  # why

    dfs(x + 1, y, empty - 1)
    dfs(x - 1, y, empty - 1)
    dfs(x, y - 1, empty - 1)
    dfs(x, y + 1, empty - 1)
    grid[x][y] = 0


m, n, empty = len(agrid), len(agrid[0]), 1
for i in range(m):
    for j in range(n):
        if agrid[i][j] == 1:
            x, y = (i, j)
        elif agrid[i][j] == 2:
            end = (i, j)
        elif agrid[i][j] == 0:
            empty += 1
res = dfs(x, y, empty)

agride = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

print(res)