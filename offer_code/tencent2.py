from itertools import combinations


class Solution:
    def solution(self, work):
        n = len(work)
        res = sum(work)
        for i in range(n // 2):
            res = min(work[n // 2 - 1] + work[n // 2 + i], res)
        return res
alist = [2, 3, 5, 5, 4, 6]
# n = int(input())
# alist = []
# for i in range(n):
#     m, n = [int(_) for _ in input().split()]
#     for i in range(m):
#         alist.append(n)
print(Solution().solution(alist))
