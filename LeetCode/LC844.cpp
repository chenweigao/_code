#include <iostream>
#include <string>
#include <stack>
using namespace std;

void func(stack<char> &buf, string &S)
{
    for (auto s : S)
    {
        if (s != '#')
        {
            buf.push(s);
        }
        else
        {
            if (!buf.empty())
                buf.pop();
        }
    }
}

int main()
{
    string S = "ab#c";
    string T = "ad#c";
    stack<char> SS, TT;

    func(SS, S);
    func(TT, T);

    // for (auto s : S)
    // {
    //     if (s != '#')
    //     {
    //         SS.push(s);
    //     }
    //     else {
    //         SS.pop();
    //     }
    // }

    // for (auto t : T)
    // {
    //     if (t != '#')
    //     {
    //         TT.push(t);
    //     }
    //     else {
    //         TT.pop();
    //     }
    // }
    bool res;
    if (SS == TT)
    {
        res = true;
    }
    cout << res << endl;
}