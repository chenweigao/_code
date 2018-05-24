#include <iostream>
#include <map>

typedef std::map<int, int> polynomial;

polynomial merge(polynomial a, polynomial b){
    polynomial result;
    for (auto i:a){
        result[i.first]=i.second;
    }

    for (auto i:b){
        result[i.first]=result[i.first]+i.second;
    }

    return result;
}


int main() {
    //std::cout << "Hello, World!" << std::endl;

    polynomial a,b;
    a[0]=0;
    a[1]=1;
    a[2]=2;

    b[1]=10;
    b[2]=20;
    b[3]=30;

    auto c=merge(a, b);

    bool plus=false;
    for(auto i:c){
        if(i.second==0)
            continue;

        if(plus)
            std::cout<<" + ";

        std::cout<<i.second<<"x^"<<i.first;
        plus= true;
    }

    std::cout<<std::endl;

    return 0;
}
