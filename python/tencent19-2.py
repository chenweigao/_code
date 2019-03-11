# n, m = input(), list(map(int, input().split()))

import sys

def getAns(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n / 2
    else:
        return (-1) * (n + 1) / 2


n = int(sys.stdin.readline().strip())
for i in range(n):
    # 读取每一行
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))
    x = values[0]
    m = values[1]
    res = int(getAns(m) - getAns(x-1))
    print(res)
    