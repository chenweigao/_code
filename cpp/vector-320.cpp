#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char const *argv[])
{
    vector<int> vec;
    for (int i; cin >> i; vec.push_back(i))
        ;

    if (vec.empty())
        return -1;
    if (vec.size() == 1)
        return -1;
    for (int i = 0; i < vec.size() - 1; ++i)
    {
        //计算相邻两个元素的和 1 2 3 4 5 --> 3 5 7 9 
        cout << vec[i] + vec[i + 1] << " ";
    } 
    cout << endl;

    auto size = (vec.size + 1) / 2;


    return 0;
}
