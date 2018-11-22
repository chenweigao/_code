#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(int argc, char const *argv[])
{
    std::vector<int> narci_arr{153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084};
    int beg, end;
    cin >> beg >> end;
    auto count = count_if(narci_arr.begin(), narci_arr.end(), [beg, end](int i) { return i >= beg && i <= end; });
    cout << count << endl;
    return 0;
}
