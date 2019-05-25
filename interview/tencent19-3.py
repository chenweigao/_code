from builtins import input
import sys
import math
str_in = input()
m, n = [int(_) for _ in str_in.split()]
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))
# def math.factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * math.factorial(n-1)

res = int(math.factorial(m) / (math.factorial(n)
                               * math.factorial(m - n))) * (m - n) * 2
print(int(res % (1e9+7)))
