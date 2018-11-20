#include <iostream>
#include <vector>
using namespace std;

auto contains(vector<int>::const_iterator first, vector<int>::const_iterator last, int value)
{
    for (; first != last; ++first)
    {
        if (*first == value)
            return first;
    }
    return last;
}

int main(int argc, char const *argv[])
{
    vector<int> v{1, 2, 3, 4, 5, 7, 8, 9};
    auto find_result = contains(v.cbegin(), v.cend(), 5);
    cout << *find_result << endl;
    return 0;
}
