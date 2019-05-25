from builtins import input


class Solution:
    def solution(self, num: str):
        res = ""
        for i in num[::-1]:
            if i not in res:
                res += i
        return res


while True:
    try:
        num = input()
        print(Solution().solution(num))

    except:
        break
# num = "9876673"
# print(Solution().solution(num))
