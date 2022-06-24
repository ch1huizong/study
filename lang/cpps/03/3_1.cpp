#include <iostream>
// T: 函数调用-1 - 数的n次方

double power(double x, int n) {
    double val = 1.0;
    while (n--) {
        val *= x;
    }
    return val;
}

int main(int argc, char *argv[]) {
    double pow;
    pow = power(5, 2);
    std::cout << "5 to the power 2 is " << pow << std::endl;

    return 0;
}
