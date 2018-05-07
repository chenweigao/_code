#include <iostream>
#include <string>
#include <sstream>
using namespace std;
int main(){
    string mystr;
    int price=0;

    while(getline(cin, mystr)){
    stringstream(mystr) >> price;
    cout << price <<endl;
    }

}