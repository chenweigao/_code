#include <iostream>
#include <vector>
using namespace std;

class Solutiion
{
  public:
    int removeDuplicates(vector<int> &nums)
    {
        int slow = 1;
        for (int fast = 1; fast < nums.size(); fast++)
        {
            if (nums[slow - 1] != nums[fast])
            {
                nums[slow++] = nums[fast];
            }
        }
        return slow < nums.size() ? slow : nums.size();
    }
};
int main()
{
    vector<int> nums = {0, 0, 1, 1, 2, 3, 4, 4};
    int ret = Solutiion().removeDuplicates(nums);
    cout << ret << endl;
    system("pause");
    return 0;
}
