n = -53

ans = ''
l = -90
r = 90

for i in range(6):
    mid = int((l + r) / 2)
    if mid <= n:
        ans += '1'
        l = mid
    else:
        ans += '0'
        r = mid

print(ans)