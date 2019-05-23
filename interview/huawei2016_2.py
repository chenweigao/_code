import collections

dic = collections.OrderedDict()

while True:
    try:
        s = input()

        index = s.rfind('\\')
        filename=s[index + 1:]
        if filename in dic:
            dic[filename] += 1
        else:
            dic[filename] = 1
    except:
        break

dic_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)



for items in dic_list[:8]:
    print(items[0].split()[0][-16:], items[0].split()[1], items[1])
