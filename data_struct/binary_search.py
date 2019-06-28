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


# 使用 bisect 库
import bisect

li = [1, 3, 4, 4, 6, 7]

print(bisect.bisect(li, 4)) # 默认找到相同元素的最右侧 4
print(bisect.bisect_left(li, 4)) # 左侧 2


li2 = [1, 3, 4, 4, 6, 7]
bisect.insort(li2, 5)
print(li2) # 输出排序后的，类似于插入排序
