#include <iostream>
// #include <algorithm>
#include <string>
#include <vector>

using namespace std;

void printReverse(const char *str)
{
    if (!*str)
        return;
    printReverse(str + 1);
    putchar(*str);
}

void helper(int index, string str)
{
    if (index >= str.length())
    {
        return;
    }
    helper(index + 1, str);
    putchar(str[index]);
}
void printReverse2(string str)
{
    helper(0, str);
}

void reverseStringInplace(vector<char> &s)
{
    int start = 0, end = s.size() - 1;
    while (start < end)
    {
        swap(s[start++], s[end--]);
    }
}

int main()
{
    char s[] = "hello world";
    printReverse(s);
    std::cout << endl;
    string s1 = "this is string 1";
    // string s11;
    // getline(std::cin, s11);
    printReverse2(s1);
    std::cout << endl;
    vector<char> s2 {'h', 'e', 'l', 'l', 'o'};
    reverseStringInplace(s2);
    for(auto i : s2)
        cout << i << ',';
    cout << endl;
    return 0;
}