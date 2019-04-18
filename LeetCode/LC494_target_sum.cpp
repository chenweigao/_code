#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class Solution
{

  public:
    int findTargetSumWays(vector<int> &nums, int s)
    {
        int target = accumulate(nums.begin(), nums.end(), 0);
        if((target + s) & 1 || target < s)  
            return 0;
        target = (target + s)  >> 1;

        vector<int> dp (target + 1, 0);
        
    }
};

int main()
{
    vector<int> nums = {1, 1, 1, 1, 1};
    int s = 3;
    int res = Solution().findTargetSumWays(nums, s);
    cout << res << endl;
    return 0;
}