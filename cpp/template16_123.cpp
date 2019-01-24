#include <iostream>

using std::cout;
using std::endl;

#include <vector>
using std::vector;

template <typename T>
int compare(const T &v1, const T &v2)
{
    if (v1 < v2)
    {
        return -1;
    }
    if (v2 < v1)
    {
        return 1;
    }
    return 0;
}

int main() 
{
    cout << compare(0, 1) << endl;
    
    vector<int> vec1{1, 2, 3}, vec2{4, 5, 6};
    cout << compare(vec2, vec1) << endl;

    return 0;
}