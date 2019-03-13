def heapify(arr: list, index: int, heap_size: int):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and arr[left_index] > arr[largest]:
        largest = left_index

    if right_index < heap_size and arr[right_index] > arr[largest]:
        largest = right_index

    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, heap_size)


def heap_sort(arr):

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1): # -1 because of [)
        heapify(arr, i, n)
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(arr, 0, end - 1)
    return arr


l = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
print(heap_sort(l))  # 原地排序
