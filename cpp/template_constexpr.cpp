#include<iostream>
#include<string>

using namespace std;

// 模板参数列表之后，返回类型之前
template <typename T>
constexpr unsigned getSize(const T(&)[size]) 
{
    return size;
}
