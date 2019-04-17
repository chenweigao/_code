#include <iostream>
#include <vector>

using namespace std;

class Solution
{
  public:
    bool canPartition(vector<int> &nums)
    {
        int sum = 0;
        int n = nums.size();

        for (int num : nums)
        {
            sum += num;
        }

        if ((sum & 1) == 1)
        {
            return false;
        }

        int target = sum /= 2;

        vector<vector<bool>> dp(n + 1, vector<bool>(target + 1, false));

        dp[0][0] = true;

        for (int i = 1; i <= n; i++)
        {
            dp[i][0] = true;
        }

        for (int j = 0; j < target + 1; j++)
        {
            dp[0][j] = false;
        }

        
    }
}