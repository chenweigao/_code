class Solution:
    def solution(self, s, num):
        if len(s) < num:
            return s
        if len(s) % num != 0:
            s = s + '0' * (num - len(s) % num)
        res = []
        i = 0
        while i < len(s):
            res.append(s[i:i + num])
            i += num
        return res

line = input().strip()
s = line.split()[0]
num = int(line.split()[1])

# s = 'iamanengineer'
# num = 4
res = Solution().solution(s, num)
for _ in res:
    print(_)