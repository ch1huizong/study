#include <cmath>
#include <iostream>
// T: 使用系统函数库

const double PI = 3.14159265358979;

int main(int argc, char *argv[]) {
    double angle;
    std::cout << "Please enter an angle: ";
    std::cin >> angle;
    double radian = angle * PI / 180; //弧度

    std::cout << "sin(" << angle << ")=" << sin(radian) << std::endl;
    std::cout << "cos(" << angle << ")=" << cos(radian) << std::endl;
    std::cout << "tan(" << angle << ")=" << tan(radian) << std::endl;

    return 0;
}
