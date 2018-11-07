#include <iostream>
#include <iterator>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
    string s("this is some string!");
    for( auto it = s.begin(); it != s.end() && !isspace(*it); ++it)
        *it = toupper(*it);
    cout << s << endl;    
    return 0;
}
