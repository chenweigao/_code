class Solution:
    def solution(self, m, s):
        if len(s) < 11:
            return 'NO'
        for ch in s:
            if ch != '8':
                s = s[1:]
                m -= 1
            else:
                break
        if len(s) >= 11:
            return 'YES'
        else:
            return 'NO'

n = int(input())
for i in range(n):
    m = int(input())
    s = input()
    print(Solution().solution(m, s))