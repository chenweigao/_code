#include <iostream>
#include <vector>
#include <string>

int main(int argc, char const *argv[])
{
    std::vector<std::string> vec;
    for (std::string buffer; std::cin >> buffer; vec.push_back(buffer))
        ;
    for (auto i : vec)
    {
        // std::cout << i << std::endl;
        if (i.empty())
            std::cout << "(null)"
                      << ",";
        else
            std::cout << i << ",";
    }
    return 0;
}
