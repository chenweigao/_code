flavor_list = ['I','O','U','P']

for i, flavor in enumerate(flavor_list):
    print('%d %s' % (i, flavor))


for i, flavor in enumerate(flavor_list, 2):
    print('%d %s' % (i, flavor))
# 2 表示下标从2 开始计数， 默认为0