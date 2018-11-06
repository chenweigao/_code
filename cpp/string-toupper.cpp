#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main(int argc, char const *argv[])
{
    string str("This is a string!");
    for(auto &c: str){
        c = toupper(c);
    }
    cout << str << endl;
    return 0;
}
