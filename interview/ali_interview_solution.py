import numpy as np
datas = [[1, 12], [5, 3], [20, 7]]

shortcut_list = [[0, 10, 1], [13, 8, 2]]

# shortcut_cost = {[0, 10, 1]: 10, [13, 8, 2]: -5}

# data_cost_dic = {[1, 12]: 11, [5, 3]: -2, [20, 7]: -13}

# value_list = [10, -5]
# data_cost = [11, -2, -13]

# for 11, find the most closed value in shortcut_cost
# using binary search
def search(arr, num):
    ret = arr[0]
    distance = abs(ret - num)
    for i in range(len(arr)):
        new_distance = abs(arr[i] - num)
        if new_distance < distance:
            distance = new_distance
            ret = arr[i]
    return ret

def binarySearch(alist, value):
    start = 0
    end = len(alist) - 1
    while start + 1 < end:
        mid = (end - start) // 2
        if alist[mid] < value:
            start = mid
        else:
            end = mid
    if value - alist[start] <= alist[end] - value:
        return alist[start]
    return alist[end]




data_cost = [0] * len(datas)
for i, data in enumerate(datas):
    data_cost[i] = data[1] - data[0]

data_cost_dic = {}
for data in datas:
    data_cost_dic[data[1] - data[0]] = data
shortcut_cost = {}
for s in shortcut_list:
    shortcut_cost[(s[1] - s[0])] = (s[0], s[1], s[2])

value_list = []
for i in shortcut_cost.keys():
    value_list.append(i)


for d in data_cost:
    index = binarySearch(value_list, d)
    a = shortcut_cost[index][0]
    b = shortcut_cost[index][1]
    weight = shortcut_cost[index][2]
    start = data_cost_dic[d][0]
    end = data_cost_dic[d][1]
    res = abs(end - start)

    result = min(abs(end - b) + abs(start - a) + weight, res)
    print(result) #4 2 10