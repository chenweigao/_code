nums = [1,2,3,4,5,1,2,4,5,3,7]
no_duplicated_list = []
for i in nums:
    if i not in no_duplicated_list:
        no_duplicated_list.append(i)
    else:
        no_duplicated_list.remove(i)
print('solution one is: ',no_duplicated_list.pop())

hash_table = {}
for i in nums:
    try:
        hash_table.pop(i)
    except:
        hash_table[i] = 1
print('solution two is: ', hash_table.popitem()[0])
