from builtins import input


class Solution:
    def max_length_of_substring(self, s) -> int:
        n = len(s)
        res, temp = 1, 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                temp += 1
            else:
                temp = 1
            res = max(res, temp)
        return res


while True:
    try:
        s = input()
        print(Solution().max_length_of_substring(s))

    except:
        break
# s = '111101111'
