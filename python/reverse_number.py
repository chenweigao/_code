def reverse(x):
    sign = [1, -1][x < 0]
    res = sign * int(str(abs(x))[::-1])
    return res if -(2**31)-1 < res < 2**31 else 0


print(reverse(32344414))
