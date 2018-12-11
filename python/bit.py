
res = []
for i in range(32):
    res.append(str(12 >> i & 1))
res.reverse()
print("".join(res)) # 二进制串

int_res = int("".join(res), 2) #十进制整数

print(int_res)

res2 = 0
for i in range(31, -1, -1):
    res2 = (res2 << 1) + (12 >> i & 1)

# 从高位往低位计算，得到 12 的二进制后又转化为 10 进制

print(res2)