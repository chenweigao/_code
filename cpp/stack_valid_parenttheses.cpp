#include <iostream>
#include <stack>
#include <string>
#include <unordered_map>
#include <cctype>
#include <algorithm>
using std::string;

auto strip(string &str) -> string const &
{
    str.erase(remove_if(str.begin(), str.end(), isalnum), str.end());
    return str;
}

bool isValid(string s)
{
    std::stack<char> st;
    for (auto &c : strip(s))
    {
        if (c == '{' || c == '(' || c == '[')
            st.push(c);
        else
        {
            if (st.empty())
                return false;
            if (c == ')' && st.top() != '(')
                return false;
            if (c == ']' && st.top() != '[')
                return false;
            if (c == '}' && st.top() != '{')
                return false;
            st.pop();
        }
    }
    return st.empty();
}
int main()
{
    std::string s = "(123wer[dsaf])";
    std::cout << isValid(s);
}