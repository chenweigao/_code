from itertools import combinations
from itertools import permutations

perm = permutations([1, 2, 3], 2)


print("permutations:")
for i in list(perm):
    print(i)


comb = combinations([1, 2, 3], 2)

print("combinations:")
for i in list(comb):
    print(i)
 