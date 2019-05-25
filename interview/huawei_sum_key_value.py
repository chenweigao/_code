from builtins import input
num = int(input())

dic = {}
for i in range(num):
    k, v = map(int, input().split())

    if k in dic.keys():
        dic[k] += v
    else:
        dic[k] = v
dic_keys = sorted(dic.keys())
# print(dic)

for i in dic_keys:
    print(i, dic[i])