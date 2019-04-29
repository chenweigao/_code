class Solution:

    def myAtoi(self, s):
        ls = list(s.strip())  # remove the space at the start of sting
        if len(s) <= 0 or len(ls) <= 0:
            return 0

        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']:
            del ls[0]

        ret, i = 0, 0

        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))


s = [
    '42', '    -42', '4193 in words', '-91283472332', '91283472332'
]

for si in s:
    print(Solution().myAtoi(si))
