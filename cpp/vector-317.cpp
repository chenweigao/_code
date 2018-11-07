#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
    vector<string> vec;
    for (string word; cin >> word; vec.push_back(word))
        ;
    for (auto &str : vec)
        for (auto &c : str)
            c = toupper(c);

    for (string::size_type i = 0; i != vec.size(); ++i)
    {
        if (i != 0 && i % 8 == 0)
        // 8 words is a line
            cout << endl;
        cout << vec[i] << " ";
    }
    cout << endl;
    return 0;
}
