class Solution:
    def toHex(self, num: int) -> str:
        dic = '0123456789abcdef'

        if num == 0:
            return "0"
        res = ''

        while num != 0 and len(res) < 8:
            res = dic[(num & 15)] + res  # num & 15 == num % 16
            # 把 res 加到后面，不然要进行 reverse
            num = num >> 4 # num / 16 == num >> 4
        return res

num = -1

print(Solution().toHex(num))
