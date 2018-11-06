#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
    string line;
    while (getline(cin, line))
        if (!line.empty()) 
            cout << line << endl;
    return 0;
}
