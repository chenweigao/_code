# n, m = input(), list(map(int, input().split()))

# print(n, m)

m = [45, 12, 45, 32, 5, 6]
# m = [3,3,3,3]
m.sort()


min_val = m[1] - m[0]
min_count = 0

for i in range(1, len(m) - 1):
    min_val = min(min_val, m[i + 1] - m[i])

for i in range(len(m) - 1):
    if min_val == m[i + 1] - m[i]:
        min_count += 1

max_val = m[len(m) - 1] - m[0]
max_count = 0

if (len(set(m)) == len(m)):
    max_count = 1
elif (len(set(m)) != 1):
    min_count1 = 0
    max_count1 = 0
    for i in range(len(m)):
        if m[i] == m[0]:
            min_count1 += 1
        if m[i] == m[len(m) - 1]:
            max_count1 += 1

    max_count = min_count1 * max_count1
else:
    max_count = len(m)*(len(m)-1)/2

print(min_count, max_count)