#include <stdio.h>

// 测试函数返回一个结构
// 从函数返回多个数据项

typedef struct powers
{
    double base, square, cube;
} powers;

powers get_power(double in)
{
    powers out = {.base = in, .square = in * in, .cube = in * in * in};
    return out;
}

int main(int argc, char const *argv[])
{
    powers threes = get_power(3);
    printf("%g\t%g\t%g\n", threes.base, threes.square, threes.cube);    
    // 3  9  27
    return 0;
}
