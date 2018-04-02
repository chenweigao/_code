#include<iostream>
#include<string>
#include<vector>
using namespace std;
class Solution {
public:
    int findMaxConscutiveOnes(vector<int>& nums) {
        int max_cnt = 0, cont = 0;
        for(auto n : nums) {
            if(n==1) max_cnt = max(++cont, max_cnt);
            else cont = 0;
        }
        return max_cnt;
    }
};
int main() {
    // string line;
    // while (getline(cin, line)) {
    //     vector<int> nums = stringToIntergerVector(line);
    //     int ret = Solution().findMaxConscutiveOnes(nums);
    //     string out = to_string(ret);
    //     cout << out << endl;
    vector<int> nums = [1,1,0,1,1,1];
    int ret = Solution().findMaxConscutiveOnes(nums);
    cout << ret << endl;
    // }
    return 0;
}