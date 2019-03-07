#include <iostream>
using namespace std;
unsigned int arr[32]; // 1024 = 32 * 32

int main()
{
    int id1, id2;
    while (cin >> id1 >> id2)
    {
        if (!(id2 >= 1 && id2 <= 1024))
        {
            cout << -1 << endl;
            continue;
        }
        arr[(id1 - 1) >> 5] &= ~(1 << (id1 & 31));

        arr[(id1 - 1) >> 5] |= (1 << (id1 & 31));
        for (int i = 0; i < 32; i++)
        {
            cout << arr[i] << " ";
        }
        // cout << ((arr[(id2 - 1) >> 5] & (1 << (id2 & 31))) != 0) << endl;
    }
    return 0;
}

//arr[(id1-1)>>5] &= ~(1<<(id1&31));