def merge_sort(arr):
    start = []
    end = []

    while len(arr) > 1:
        a = min(arr)
        b = max(arr)
        start.append(a)
        end.append(b)
        arr.remove(a)
        arr.remove(b)
    if arr:
        start.append(arr[0])
    end.reverse()
    return (start + end)

arr = [1, 3, 2, 6, 4]
print(merge_sort(arr))