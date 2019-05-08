'''
given a number, for example: 5
5 4 3 2 1

1 is no use

20: 20 / 5 = 4  and 4 /5 = 0
100: 100 / 5 = 20 

all we need to do is count how many 5 we have
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        return self.trailingZeroes(n // 5) + n // 5