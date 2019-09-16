class Solution:
    def solution(self, l, r):
        count = 0
        for i in range(l, r + 1):
            if ((i + 1) * i // 2) % 3 == 0:
                count += 1
        return count

m, n = map(int, input().split())
res = Solution().solution(m, n)
print(res)

