#include <iostream>
#include <vector>
#include <limits.h>
#include <algorithm>
#include <queue>

using namespace std;

int numSquares(int n)
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
    int res = numSquares(12);
    cout << res << endl;
    return 0;
}