#include <iostream>
int main(){
    int a[] = {2,3,5,7};
    for(auto x : a){
        std::cout << x << ",";
    }
    std::cout << std::endl;
    return 0;
}