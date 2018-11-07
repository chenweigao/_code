#include <iostream>
#include <iterator>
#include <vector>
using namespace std;

int main(int argc, char const *argv[])
{
    vector<unsigned> scores(11, 0);
    for(unsigned grade; cin >> grade;)
        if(grade <= 100)
            ++*(scores.begin() + grade /10);

    for(auto s: scores)
        cout << s << " ";
    cout << endl;
    return 0;
}
