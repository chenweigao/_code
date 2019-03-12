def bubble_sort(arr:list):

    length = len(arr)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

lists = [-23, 0, 6, -4, 34]
print(bubble_sort(lists))