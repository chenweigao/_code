// exercise 3.5
#include <iostream>
#include <string>
using namespace std;
int main(int argc, char const *argv[])
{
    string res, word;
    while (cin >> word && word != "q")
    {
        res = res + word + ' ';
    }
    cout << res << endl;
    return 0;
}
