#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>
using namespace std;

// buttom-top
int minimumTotal(vector<vector<int>> &triangle)
{
    int n = triangle.size();
    vector<int> dp(triangle.back()); // 该行代码将 triangle 的最后一行元素全部赋值给了 dp, 所以和下面两种解法的赋值方法不同
    for (int layer = n - 1 -1; layer >= 0; layer--)
    {
        for (int i = 0; i <= layer; i++)
        {
            dp[i] = std::min(dp[i + 1], dp[i]) + triangle[layer][i];
        }
    }
    return dp[0];
}

// top-buttom
int minimumTotal2(vector<vector<int>> &triangle)
{
    if (triangle.size() == 0)
    {
        return 0;
    }
    vector<vector<int>> dp;
    // 注意在初始化的时候是根据 triangle 的大小去初始化 dp 数组的
    for (int i = 0; i < triangle.size(); i++)
    {
        dp.push_back(vector<int>());
        for (int j = 0; j < triangle[i].size(); j++)
        {
            dp[i].push_back(0);
        }
    }

    dp[0][0] = triangle[0][0];
    for (int i = 1; i < dp.size(); i++)
    {
        dp[i][0] = triangle[i][0] + dp[i - 1][0];                                                  // 每行第一个元素的递推
        dp[i][dp[i].size() - 1] = triangle[i][dp[i].size() - 1] + dp[i - 1][dp[i].size() - 1 - 1]; // 每行最后一个元素的递推，注意每一行的元素不相等
        for (int j = 1; j < dp[i].size() - 1; j++)
        {
            dp[i][j] = triangle[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1]);
        }
    }
    int result = INT_MAX;
    for (int i = 0; i < dp[dp.size() - 1].size(); i++)
    {
        result = min(result, dp[dp.size() - 1][i]);
    }
    return result;
}

// buttom-up version2
int minimumTotal3(vector<vector<int>> & triangle)
{
    if (triangle.size() == 0) {
        /* code */
        return 0;
    }
    vector<vector<int>> dp;
    for(int i = 0; i < triangle.size(); i++)
    {
        dp.push_back(vector<int>());
        for(int j = 0; j < triangle[i].size(); j++)
        {
            dp[i].push_back(0);
        }
    }
    for(int i = 0; i < dp[dp.size()-1].size(); i++)
    {
        dp[dp.size() - 1][i] = triangle[dp.size() - 1][i]; // 计算出最后一行的初始值
    }
    
    for (int i = dp.size()-1-1; i >= 0;i--)
    {
        for(int j = 0; j < dp[i].size(); j++)
        {
            dp[i][j] = triangle[i][j] + min(dp[i + 1][j + 1], dp[i + 1][j]);
        }
        
    }

    return dp[0][0];
}

int main()
{
    vector<vector<int>> triangle;
    triangle.push_back({2});
    triangle.push_back({3, 4});
    triangle.push_back({6, 5, 7});
    triangle.push_back({4, 1, 8, 3});

    int res = minimumTotal(triangle);
    cout << "res1 is " << res << endl;

    int res2 = minimumTotal3(triangle);
    cout << "res2 is " << res2 << endl;
    return 0;
}