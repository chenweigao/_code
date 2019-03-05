#include <iostream>
#include <vector>
using namespace std;

vector<int> addToArrayForm(vector<int> &A, int K)
{
    for (int i = A.size() - 1; i >= 0&& K > 0; i--)
    {
        A[i] += K;
        K = A[i] / 10;
        A[i] %= 10;
    }
}

int main()
{
    vector<int> A = {1, 2, 0, 0};
    vector<int> result = addToArrayForm(A, 34);
    for (auto &r : result)
    {
        cout << r << endl;
    }
}
