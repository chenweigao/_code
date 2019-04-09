#include <iostream>
#include <vector>
#include <limits.h>
#include <algorithm>

using namespace std;

int numSequares(int n)
{
    if (n <= 0)
    {
        return 0;
    }
    vector<int> dp = {0};

    while(dp.size() <= n)
    {
        int tmp = INT_MAX;
        int m = dp.size();
        for (int j = 1; j * j <= m; j++)
        {
            tmp = min(tmp, dp[m - j * j] + 1);
        }
        dp.push_back(tmp);
    }
    return dp[n];
}

int main()
{
    int n = 12;
    int res = numSequares(12);
    cout << res << endl;
    return 0;
}