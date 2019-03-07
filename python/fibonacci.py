# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

# Recursive approach
def fib_recur(n):
    if n < 2:
        return  n
    return fib_recur(n-1) + fib_recur(n-2)


# dynamic programmming approach
def fib_dyn(n):
    if n < 2:
        return n 
    memo = [-1 for i in range(n+1)]
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]

# imperative approach
def fib_imp(n):
    if n < 2:
        return n
    a = 0
    b = 1
    for i in range(1, n):
        a, b = b, a + b
    return b
