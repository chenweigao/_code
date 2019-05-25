from builtins import input


class Solution:
    def closestInteger(self, num: float) -> int:
        integer_part = int(num)
        decimal_part = num - int(num)

        res = 0
        if decimal_part >= 0.5:
            res = integer_part + 1
        else:
            res = integer_part
        return res


# num = 5.5
# print(Solution().closestInteger(num))
while True:
    try:
        num = float(input())
        print(Solution().closestInteger(num))
    except:
        break
