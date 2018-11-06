#include <iostream>
#include <string>
#include <cctype>
using namespace std;
int main(int argc, char const *argv[])
{
    string str("some string!!!@#!");
    decltype(str.size()) punct_cnt = 0;
    for (auto c : str)
    {
        if (ispunct(c))
        {
            ++punct_cnt;
        }
    }
    cout << punct_cnt << " punctuation characters in" << str << endl;
    return 0;
}