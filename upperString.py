# leetcode 784
s = "a1b2"
print(s.upper())
res = ['']
for ch in s:
    if ch.isalpha():
        res = [ i+j for i in res for j in [ch.upper(), ch.lower()]]
    else:
        res = [i+ch for i in res]
return res