#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s = "PLPALL";
    int absent = 0, late = 0;
    for (auto &ss : s)
    {
        cout << ss << endl;
        if (ss == 'A')
        {
            absent++;
        }
        if (ss == 'L')
        {
            late++;
        }
        else late = 0;
    }
    if (absent >= 2 || late > 2)
    {
        cout << "no";
    }
    else
        cout << "yes";
}