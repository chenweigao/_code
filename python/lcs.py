import sys

def lcs(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    mylist = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                mylist[i][j] = mylist[i - 1][j - 1] + 1
            else:
                mylist[i][j] = max(mylist[i][j - 1], mylist[i - 1][j])
    return mylist[len1][len2]

def reverseString(s):
    return s[::-1]

while True:
    s = sys.stdin.readline().strip()
    if not s:
        break
    
    print(len(s) - lcs(s, reverseString(s)))