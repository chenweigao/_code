from heapq import *

from heapq import _heapify_max
# 1. include index 0
# 2. pop method returns the smallest item


def heapsort(iterable):
    h = []
    for values in iterable:
        heappush(h, values)
    return [heappop(h) for i in range(len(h))]


print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

alist = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

_heapify_max(alist)

print(alist)
# heapify(alist)

# heapsort(alist)

heapreplace(alist, 10)

merged = merge([1, 2, 3, 4], [2, 3, 6, 7])

print([_ for _ in merged])

print(nlargest(3, alist))
print(nsmallest(3, alist))
