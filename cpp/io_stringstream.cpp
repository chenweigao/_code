#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{   
    int string_int = 0;
    stringstream s;
    string string_num("1234");
    s << string_num;
    s >> string_int;
    std::cout << string_int - 1 << std::endl;
    return 0;
}
