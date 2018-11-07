#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<unsigned> scores(11, 0);
    unsigned grades;
    while (cin >> grades)
    {
        if (grades <= 100)
        {
            ++scores[grades / 10];
        }
    }
}