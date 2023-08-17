#include <iostream>
// T: 内联函数

const double PI = 3.14159265358979;

inline double calArea(double radius) { return PI * radius * radius; }

int main(int argc, char *argv[]) {
    double r = 3.0;
    double area = calArea(r);
    std::cout << area << std::endl;

    return 0;
}
