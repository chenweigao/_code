class Solution:
    def solution(self, work, ability):
        res = []
        for i in range(len(ability)):
            temp = 0
            for k, v in work.items():
                if ability[i] >= k:
                    temp = max(temp, v)
            res.append(temp)
        return res


m, n = map(int, input().split())

work = {}
for i in range(m):
    a, b = map(int, input().split())
    work[a] = b
line = input().split()
ability = [int(_) for _ in line]
# work = {1:100, 10:1000, 1000000000:1001}
# ability = [9, 10, 1000000000]

res = Solution().solution(work, ability)
for _ in res:
    print(_)

