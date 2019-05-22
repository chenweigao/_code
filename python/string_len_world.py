s = input()

r_index = s.rfind(' ')

if r_index == -1:
    res = len(s)
else:
    res = len(s[r_index:]) - 1

print(res)