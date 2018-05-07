#include <iostream>

int minstep = -1;
int n = 1;
int ming = -1;
void f(int step, int g, int j)
{
    if (g == n)
    {
        if (step < minstep)
            minstep = step;
        ming = g;

        return;
    }
    if (step > minstep || g > ming)
        return;

    f(step + 1, g * 2, g);
    f(step + 1, g + j, j);
}

int main()
{
    while (!std::cin.eof())
    {
        int T = 0;
        std::cin >> T;
        while (T--)
        {
            std::cin >> n;
            minstep = n;
            ming = n;
            f(0, 1, 1);
            std::cout << minstep << std::endl;
        }
    }
    return 0;
}
