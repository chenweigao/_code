from builtins import input


class Solution:
    def solution(self, str1, str2):
        res1 = [str1[i:i + 8] for i in range(0, len(str1), 8)]
        res2 = [str2[i:i + 8] for i in range(0, len(str2), 8)]

        res = res1 + res2

        for i in range(len(res)):
            if len(res[i]) < 8:
                res[i] += '0' * (8 - len(res[i]))
            else:
                continue
        return res


# str1 = 'abc'
# str2 = '123456789'

# print(Solution().solution(str1, str2))

while True:
    try:
        str1 = input()
        str2 = input()
        res = Solution().solution(str1, str2)
        for s in res:
            print(s)
    except:
        break
