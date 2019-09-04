# 先小于后大于，先左边(l)后右边(r)
def binarySearch(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False

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
