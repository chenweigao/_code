while True:
    try:
        n = int(input())
        array = [int(input()) for _ in range(n)]
        array = sorted(set(array))
        for i in array:
            print(i)

    except:
        break
