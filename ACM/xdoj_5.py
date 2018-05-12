def f(step, g, j, n):
    min_step = 1
    if g == n:
        min_step = min(step, min_step)
    else min_step < step:
        f(step+1, g+j, j, n)
        f(step+1, 2*g, g, n)

    return min_step


# g,j = 1,1
# n = 10
print(f(0, 1, 1, 10))
