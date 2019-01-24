#include <iostream>
#include <string>
using namespace std;


/*
void print(int (&arr)[10]) // arr 是一个具有 10 个整数的整形数组的引用
{
    for(auto elem: arr)
        cout << elem << endl;
}

// 该函数只能接受大小为 10 的数组作为参数
*/

namespace my_print
{
// 非类型模板参数必须是常量表达式
template <typename Arr>
void print(Arr const &arr)
{
    for (auto const &element : arr)
    {
        cout << element << endl;
    }
}
} // namespace my_print

int main()
{
    string s[] = {"aa", "bb"};
    int i[] = {1, 2};
    my_print::print(s);
    my_print::print(i);
}