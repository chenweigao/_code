#include <iostream>
#include <string>

using namespace std;

class Solution
{
  public:
    int strStr(string hatstack, string needle)
    {
        int i = 0, j = 0;
        while (i < hatstack.size() && j < needle.size())
        {
            if (hatstack[i] == needle[j])
            {
                i++;
                j++;
            }

            else
            {
                i = i - j + 1;
                j = 0;
            }
        }
        if (j == needle.size())
            return i - j;
        else
        {
            return -1;
        }
    }
};

int main()
{
    string str1 = "helloo";
    string str2 = "ll";
    int res = Solution().strStr(str1, str2);
    cout << res << endl;
    return 0;
}