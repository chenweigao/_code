#include <iostream>
#include <unordered_map>

using namespace std;

int fib(int N)
{
    unordered_map<int, int> cache;
    int result;
    if (cache.find(N) != cache.end())
    {
        // if(cache.count(N) == 0)
        return cache[N];
    }

    if (N < 2)
        result = N;
    else
        result = fib(N - 1) + fib(N - 2);
    cache[N] = result;
    cache.insert(pair<int, int>(N, result));

    return result;
}

int main()
{
    int n = 20;
    cout << fib(n) << endl;
    return 0;
}
