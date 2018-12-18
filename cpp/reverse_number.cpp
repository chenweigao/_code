#include <limits.h>
class Solution
{
  public:
    int reverse(int x)
    {
        long long res = 0;
        while (x)
        {
            res = res * 10 + x % 10;
            x /= 10;
        }
        return (res < INT_MIN || res > INT_MAX) ? 0 : res;
    }
};

//`INT_MIN` (-2^31-1) and `INT_MAX`(2^31), defined in `<limits.h>`.
