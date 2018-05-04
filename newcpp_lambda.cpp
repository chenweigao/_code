#include<iostream>

auto f1 = [](int x) {
    return x*x;
};

int main() {
    std::cout << f1(3) << std::endl;
}