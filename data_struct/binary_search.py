def binarySearch(alist, value):
    first = 0
    last = len(alist) - 1

    mid = (last // 2)

    while binarySearch:
        if value == alist[mid]:
            return mid
        else:
            if value < mid:
                last = mid - 1
            else:
                if value > mid:
                    first = mid + 1
        return -1


def binarySearch2(arr, l, r, x):
    if r >= l:
        mid = (r + l) // 2
        if(arr[mid] == x):
            return mid
        if(arr[mid] > x):
            return binarySearch2(arr, 0, mid - 1, x)
        return binarySearch2(arr, mid + 1, r, x)
    else:
        return -1


print(binarySearch2([1, 2, 3, 4, 5, 6], 0, 5, 3))


alist = [-3, -5, 9, 10, 13]
value = 11
print(rIndex(alist, value))
