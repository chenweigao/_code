#include <cstring>
#include <iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    const char ca[] = {'h', 'e', 'l', 'l', 'o','\0'};
    const char *cp = ca;
    while(*cp) {
        cout << *cp << endl;
        ++cp;
    }
    return 0;
}
//该程序导致了越界问题，原因在于ca[]中未定义结束的空字符'\0'