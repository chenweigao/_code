# s = 'google'
from itertools import accumulate


def isPalin(s):
    if s == s[::-1] and len(s) != 0:
        return True
    return False


def getAllSubstring(s: str):
    sub_list = []
    for i in range(len(s)):
        sub_list.append(s[0:i] + s[i + 1:])
    return sub_list


while True:
    s = input()
    sum = 0
    slist = []
    for i in range(0, len(s)+1):
        slist = slist + getAllSubstring(s[:i])
    print(slist)
    for i in slist:
        if isPalin(i):
            sum = max(sum, len(i))
            print(sum)
    print(len(s) - sum)
