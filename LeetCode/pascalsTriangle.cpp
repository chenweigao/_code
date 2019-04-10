#include <iostream>
#include <vector>

using namespace std;

class Solution
{
  public:
    vector<vector<int>> generate(int numRows)
    {
        vector<vector<int>> res(numRows, vector<int>());
        for (int i = 0; i < res.size(); i++)
        {
            res[i].resize(i + 1);
            res[i][0] = res[i][i] = 1;

            for (int j = 0; j < i; j++)
            {
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j];
            }
        }
        return res;
    }

    vector<int> getRow(int rowIndex)
    {
        vector<int> res(rowIndex + 1, 0);
        res[0] = 1;
        for (int i = 1; i < res.size(); i++)
        {
            for (int j = i; j >= 1; j--)
            {
                res[j] += res[j - 1];
            }
        }
        return res;
    }
};

int main()
{
    vector<vector<int>> res(4);
    return 0;
}