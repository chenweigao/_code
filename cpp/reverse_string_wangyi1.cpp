#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

string reverseWords(string s)
{
    string cleanString = "";
    bool wasSpace = true;
    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] != ' ')
        {
            cleanString += s[i];
            wasSpace = false;
        }
        else
        {
            if (wasSpace == false)
                cleanString += s[i];
            wasSpace = true;
        }
    }
    if (cleanString.size() > 0)
    {
        int lastIdx = cleanString.size() - 1;
        if (cleanString[lastIdx] == ' ')
        {
            cleanString.pop_back();       
        }

    }

    int start = 0;
    int cur;
    for (cur = 0; cur < cleanString.size(); cur++)
    {
        if (!isalnum(cleanString[cur]))
        {
            reverse(cleanString.begin() + start, cleanString.begin() + cur);
            start = cur + 1;
        }
    }
    reverse(cleanString.begin() + start, cleanString.begin() + cur);
    reverse(cleanString.begin(), cleanString.end());
    return cleanString;

}

int main()
{
    string s;
    // getline(std::cin, s);
    s = "This: is a list.";
    string res = reverseWords(s);
    cout << res << endl;
    return 0;
}