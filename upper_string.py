# leetcode 784
# product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
# product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
s = 's1w3e'
import itertools
class Solution:
    def letterCasePermutation(self, S):
        L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
        return [''.join(i) for i in itertools.product(*L)]

S = Solution().letterCasePermutation(s)
print(S)
# print([[i.upper(), i.lower()] for i in 'we32e'])
# [['W', 'w'], ['E', 'e'], ['3', '3'], ['2', '2'], ['E', 'e']]