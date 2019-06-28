def fib(limit):
    a, b = 0, 1

    while a < limit:
        yield a
        a, b = b, a+b

for i in fib(10):
    print(i)