from heapq import merge


def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        middle = len(seq) // 2
        left = merge_sort(seq[:middle])
        right = merge_sort(seq[middle:])
        # return list(merge(left, right))
        return my_merge(left, right)


def my_merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
        
    result += left[l:]
    result += right[r:]
    return result


seq = [1, 3, 6, 2, 4, 0, -1, 3]
print(merge_sort(seq))
