A = [1, 2, 0, 0]
K = 34

def list2int(l):
    return int(''.join(list(map(str, l))))

def int2list(i):
    return list(map(int, str(i)))
print(int2list(list2int(A)+34))