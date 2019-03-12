def qsort(arr):
    if not arr:
        return []
    else:
        pivot = arr[0]
        l = [_ for _ in arr if _ < pivot]
        r = [_ for _ in arr[1:] if _ >= pivot]
        return qsort(l) + [pivot] + qsort(r)

a = [4, 65, 2, -31, 0, 99, 83, 782, 1]

print(qsort(a))