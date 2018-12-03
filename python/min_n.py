# Returns the n minimum elements from the provided list. 
# If n is greater than or equal to the provided list's length, then return the original list(sorted in ascending order).
from copy import deepcopy


def min_n(lst, n=1):
    numbers = deepcopy(lst)
    numbers.sort()
    return numbers[:n]


print(min_n([1, 3, 2, 6])) #[1]
print(min_n([1, 3, 2, 6], 2)) #[1, 2]
