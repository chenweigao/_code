#include<iostream>
using namespace std;

template <typename T>
T GetMax (T a, T b) {
	T result;
	result = (a > b)? a : b;
	return result;
}

template <class T, class U>
T GetMin (T a, U b) {
	return (a<b? a:b);
}

int main() {
	int i=5, j=6, k;
	long l=10, m=5, n;
	k = GetMax<int>(i, j);
	n = GetMax<long>(l, m);
	cout << k << endl;
	cout << n << endl;
	int ii;
	ii = GetMin(j, m);
	cout << ii << endl;
	return 0;
	// 6 10 5
}
