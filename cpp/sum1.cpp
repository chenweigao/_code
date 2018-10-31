#include <stdio.h>
#include <time.h>
int fun1(int n)
{
    int i, sum = 0;
    for (i = 1; i <= n; i++)
    {
        sum = sum + i;
    }
    return sum;
}

int fun2(int n)
{
    return n * (n + 1) / 2;
}

int main()
{
    clock_t c1, c2, c3;
    int n = 99999998;
    c1 = clock();
    int f1 = fun1(n);
    c2 = clock();
    int f2 = fun2(n);
    printf("%d,%d\n",f1, f2);
    printf("%ld\n", c2 - c1);
    printf("%ld\n", c3 - c2);
    return 0;
}