#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
    const string hexdigits = "0123456789ABCDEF";
    cout << "Enter a series of numbers between 0 and 15" << endl;
    string result; //用于保存十六进制的字符串
    string::size_type n;
    //string::size_type为无符号数，可以确保下标不会小于0
    while (cin >> n)
    {
        if( n < hexdigits.size())
            result += hexdigits[n];
    std::cout << "hex result is " << result << endl;
    }
    return 0;
}
