while True:
    try:
        n = input()
        l = list(map(int, input().split()))

        l = sorted(l)

        res = 0

        res = max(res, l[0]*l[1]*l[-1], l[-1]*l[-2]*l[-3])
        print(res)
    except:
        break