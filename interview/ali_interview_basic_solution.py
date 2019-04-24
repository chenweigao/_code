import sys

str_in = input()
n, m = [int(_) for _ in str_in.split()]

lines = []
for line in sys.stdin:
    list_new = line.split()

    list_new = [int(_) for _ in list_new]
    lines.append(list_new)
shortcut_list = []
for i in range(n):
    shortcut_list.append(lines[i])
datas = []
for j in range(m):
    datas.append(lines[j + n])

for data in datas:
    start = data[0]
    end = data[1]
    points = set()
    for s in shortcut_list:
        points.add(s[0])
        points.add(s[1])
    points.add(start)
    points.add(end)
    points = list(points)
    res = abs(end - start)


    for s in shortcut_list:
        res = min(res, abs(s[0] - start) + abs(s[1] - end) + s[2])
    print(res)
