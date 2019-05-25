from builtins import input


class Solution:
    def min_value_of_string(self, s, n) -> int:
        dic = {}
        # value = 0
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1

        # for k, v in dic.items():
        #     value += v ** 2

        arr = sorted(dic.values())

        for i in range(n):
            arr[-1] -= 1
            arr.sort()

        return sum([x ** 2 for x in arr])


while True:
    try:
        s = input()
        k = int(input())
        print(Solution().min_value_of_string(s, k))
    except:
        break


# s = 'abaccc'
# k = 1
# print(Solution().min_value_of_string(s, k))
