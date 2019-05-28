# class Solution:
#     def removeOuterParentheses(self, S: str) -> str:
#         res, opened = [], 0
#         for c in S:
#             if c == '(' and opened > 0:
#                 print(opened)
#                 res.append(c)

#             if c == ')' and opened > 1:
#                 print(opened)
#                 res.append(c)

#             opened += 1 if c == '(' else - 1

#         return ''.join(res)


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        res = ''

        for c in S:
            if c == ')':
                count -= 1
            if count > 0:
                res += c
            if c == '(':
                count += 1
        return res

S = "(()())(())"

print(Solution().removeOuterParentheses(S))
