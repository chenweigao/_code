#include <iostream>
#include <iterator>
#include <vector>
using namespace std;

int main(int argc, char const *argv[])
{
    // vector<int> v{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    vector<int> v;
    for (int i = 0; i < 10; i++)
        v.push_back(i);
    for (auto it = v.begin(); it != v.end(); ++it)
        *it *= 2;
    for (auto i : v)
        cout << i << " ";
    cout << endl;
    return 0;
}