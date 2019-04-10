#include <iostream>
#include <vector>

using namespace std;

int days, numbers;

int get_sum(int number)
{
    int sum = 0;
    for (int i = 0; i < days; i++)
    {
        sum += number;
        number = (number + 1) / 2;
    }
    return sum;
}

int binarySearch()
{
    int l = 1, r = numbers;
    int mid, res = -1;
    while (l <= r)
    {
        mid = l + (r - l) / 2;
        if (get_sum(mid) == numbers) return mid;
        if(get_sum(mid) > numbers){
            r = mid - 1;
        }
        else
        {   
            l = mid + 1;
        }
    }
    res = mid;
    return res;
}

int main()
{
    cin >> days >> numbers;

    vector<int> target_list;

    for(int i = 0; i < numbers; i++) {
        target_list.push_back(get_sum(i));
    }

    int result = binarySearch();
    cout << result << endl;
    return 0;
}