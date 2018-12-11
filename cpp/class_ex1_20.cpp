#include <iostream>
#include "Sales_item.h"

using std::cin;
using std::cout;
using std::endl;

int main()
{
    for (Sales_item item; cin >> item; cout << item << endl);
    // ISBN号、售出的册数、销售价格
    return 0;
}