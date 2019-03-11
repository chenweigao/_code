s = 'AkleBiCeilD'

res = ''
def isUpper(c):
    if ord(c) >= 65 and ord(c) <= 90:
        return True
    return False


def isLower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False


for i in s:
    if isLower(i):
        res += i

for i in s:
    if isUpper(i):
        res += i
print(res)