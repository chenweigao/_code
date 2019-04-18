#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class SolutionDP
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

        int target = sum / 2;

        vector<vector<bool>> dp(n + 1, vector<bool>(target + 1, false));

        dp[0][0] = true; // 0 element could reach 0 sum

        for (int i = 1; i <= n; i++)
        {
            dp[i][0] = true; // any element could reach 0 sum
        }

        for (int j = 0; j < target + 1; j++)
        {
            dp[0][j] = false; // 0 element could not reach any sum
        }

        // then we compute the dp array's value
        // where dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i - 1]]
        for (int i = 1; i <= n; i++)
            for (int j = 1; j < target + 1; j++)
            {
                if (j >= nums[i - 1])
                    dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i - 1]];
                else
                    dp[i][j] = dp[i - 1][j];
            }
        return dp[n][target];
    }
};

class SolutionSmallerDP
{
  public:
    bool canPartition(vector<int> &nums)
    {
        int sum = 0;
        for (auto &num : nums)
        {
            sum += num;
        }
        if ((sum & 1) == 1) // sum % 2 == 1
            return false;

        int target = sum / 2;
        vector<bool> dp(target + 1, false);
        dp[0] = true;

        for (int num : nums)
            for (int i = target; i > 0; i--)
            {
                if (i >= num)
                    dp[i] = dp[i] || dp[i - num];
            }
        return dp[target];
    }
};

class SolutionFaster
{
  public:
    bool helper(vector<int> nums, int target, int level)
    {
        if (level == nums.size())
            return false;
        if (nums[level] == target)
            return true;
        if (target < nums[level])
            return false;
        return helper(nums, target - nums[level], level + 1) || helper(nums, target, level + 1);
    }
    bool canPartition(vector<int> nums)
    {
        int target = 0;
        for (int num : nums)
        {
            target += num;
        }

        if (target % 2)
            return false;

        sort(nums.begin(), nums.end(), [](int a, int b) { return a > b; });
        // reverse(nums.begin(), nums.end());

        target /= 2;
        return helper(nums, target, 0);
    }
};
int main()
{
    vector<int> nums = {1, 5, 11, 5};
    bool res;
    res = SolutionDP().canPartition(nums);
    cout << res << endl;
    bool res2 = SolutionFaster().canPartition(nums);
    cout << "res of dfs: " << res2 << endl;
    return 0;
}