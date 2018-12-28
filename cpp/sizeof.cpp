#include<iostream>
using namespace std;
struct stu
{
	char name[22];
	long int n;
	int score[4];
} a ;

int main(){
	cout << sizeof(a) <<endl;
	cout << "size of long int: " << sizeof(long int) << endl;
	cout << "size of int: " << sizeof(int) << endl;
	cout << "size of char: " << sizeof(char) << endl;
	cout << "size of name: " << sizeof(a.name) <<endl;
	//40 4 4 1
	int arr[32];
	cout << "sizeof array arr:" << sizeof(arr)/sizeof(int) << endl;
	return 0;
}

