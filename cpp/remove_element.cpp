#include <vector>
#include <string>
#include <iostream>

using std::cout;
using std::vector;

int removeElement(vector<int> &nums, int val)
{
    int n = nums.size();
    for (int i = nums.size() - 1; i >= 0; i--)
    {
        if (nums[i] == val)
        {
            nums[i] = nums[n-1];
            n--;
        }
    }
    return n;
}

int main()
{
    vector<int> nums = {0,1,2,2,3,0,4,2};
    int len = removeElement(nums, 2);
    for (int i = 0; i < len; i++)
    {
        cout << nums[i] << "\n";
    }
}