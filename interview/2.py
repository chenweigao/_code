# n, m = input(), list(map(int, input().split()))

from itertools import permutations
from functools import reduce
from itertools import combinations,filterfalse


def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


def gcd(*args):
    numbers = []
    numbers.extend(spread(list(args)))

    def _gcd(x, y):
        return x if not y else gcd(y, x % y)

    return reduce(lambda x, y: _gcd(x, y), numbers)


res = 0

m = [_ for _ in range(200)]

for _ in combinations(m, 3):
    # print(_)
    if gcd(list(_)) == 1:
        # print(_)
        res += 1
print(res)
