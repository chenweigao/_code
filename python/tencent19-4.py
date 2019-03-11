import sys
import math
str_in = input()
m, n = [int(_) for _ in str_in.split()]

def isVaild(arr):
    for i in arr:
        if i == 1:
            continue
        return True
    return False

for i in range(m):
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    count = 0
    alist = [[0] * n]
    for i in range(m+1):
        if (alist[values[i]] != 1):
            count += 1
            alist[values[i]] = 1

print(count)
