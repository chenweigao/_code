#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string reverseWords(string s)
{
    int start = 0;
    for (int cur = 0; cur <= s.size(); cur++)
    {
        if (s[cur] == ' ' || cur == s.size())
        {
            reverse(s.begin() + start, s.begin() + cur);
            start = cur + 1;
        }
    }

    return s;
}

int main()
{
    string s = "This is a string";
    cout << reverseWords(s) << endl;
    return 0;
}