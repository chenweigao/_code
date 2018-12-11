#include <iostream>
#include "Sales_item.h"

int main(int argc, char const *argv[])
{
    Sales_item currItem, valItem;
    if (std::cin >> currItem)
    {
        int cnt = 1;
        while (std::cin >> valItem)
        {
            if (valItem.isbn() == currItem.isbn())
            {
                ++cnt;
            }
            else
            {
                std::cout << currItem << cnt << std::endl;
                currItem = valItem;
                cnt = 1;
            }
        }
        std::cout << currItem << cnt << std::endl;
    }
    return 0;
}
