#include <iostream>
#include <vector>
#include <iterator>
#include <list>
using namespace std;

int main(int argc, char const *argv[])
{
    list<int> list(5, 4);
    vector<double> dvc(list.begin(), list.end());
    for (auto i : dvc)
        cout << i << " ";
    cout << endl;
    for (auto i : list)
        cout << i << " ";
    cout << endl;

    vector<int> ivc(5, 5);
    vector<double> dvc2(ivc.begin(), ivc.end());
    for (auto i : dvc2)
        cout << i << " ";
    cout << endl;
    for (auto i : ivc)
        cout << i << " ";
    cout << endl;
    return 0;
}
