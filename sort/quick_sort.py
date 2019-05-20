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

def partition(arr, first, last):
​    pivot = first
​    for pos in range(first, last):
​        if arr[pos] < arr[last]:
​            arr[pos], arr[pivot] = arr[pivot], arr[pos]
​            pivot += 1
​    arr[pivot], arr[last] = arr[last], arr[pivot]
​    return pivot

def qucik_sort(arr, first, last):
​    if first < last:
​        pi = partition(arr, first, last)
​        qucik_sort(arr, first, pi-1)
​        qucik_sort(arr, pi+1, last)

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
qucik_sort(A, 0, len(A) - 1)
print(A)