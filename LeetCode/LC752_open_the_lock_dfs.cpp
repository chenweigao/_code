#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <vector>

using namespace std;

int openLock(vector<string> &deadends, string target)
{
    // visited is a set including strings in deadends
    unordered_set<string> visited(deadends.begin(), deadends.end()); 

    if (visited.find("0000") != visited.end() || visited.find(target) != visited.end())
        return -1;

    vector<string> res;

    for (int i = 0; i < target.length(); i++)
    {
        string tmp = target;
        char pre = target[i] == '0' ? '9' : target[i] - 1;
        swap(tmp[i], pre);
        if (visited.count(tmp) == 0)
            res.push_back(tmp);

        char next = target[i] == '9' ? '0' : target[i] + 1;
        swap(tmp[i], next);
        if (visited.count(tmp) == 0)
            res.push_back(tmp);
    }


    if (res.empty())
        return -1;

    int ret = 40;

    for (auto &r : res)
    {
        int temp = 0;
        for(int i = 0; i < 4; i++)
        {
            int turns = r[i] - '0';
            if(turns > 5 )
                turns = 10 - turns;
            temp += turns;
        }
        if(temp < ret)
            ret = temp;
    }
    return ret + 1;
}

int main()
{
    string target = "0202";

    vector<string> deadends = {"0201", "0101", "0102", "1212", "2002"};

    openLock(deadends, target);

    return 0;
}