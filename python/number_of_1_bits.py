res = []
for i in range(32):
    res.append(str(12 >> i & 1))

print(res.count('1'))

# Solution 2:
count = 0
n = 12

while(n):
    n &= (n-1)
    count += 1

print(count)