#include <iostream>
// T: 函数调用-2 - 二进制转十进制

double power(double x, int n);

int main(int argc, char *argv[]) {
    int value = 0;
    std::cout << "Enter an 8 bit binary number:";

    for (int i = 7; i >= 0; i--) {
        char ch;
        std::cin >> ch;

        if (ch == '1') {
            value += static_cast<int>(power(2, i));
        }
    }

    std::cout << "Decimal value is " << value << std::endl;

    return 0;
}

double power(double x, int n) {
    double val = 1.0;
    while (n--) {
        val *= x;
    }
    return val;
}
