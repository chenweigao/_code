#include<iostream>


auto f1 = [](int x) {
    return x*x;
};
//表达式结束需要用分号
auto f2 = [](std::string s) {
    std::cout << s << std::endl;
};

auto f3 = [](int x, int y) {
    return x < y;
};

int main() {
    std::cout << f1(3) << std::endl;
    f2("heavy rain");
    std::cout << f3(1, 5) << std::endl;
}