#include <cmath>
#include <iostream>
// T: cmath库的使用

int main(int argc, char *argv[]) {
    int x, y;

    std::cout << "Enter int x: ";
    std::cin >> x;

    std::cout << "Enter int y: ";
    std::cin >> y;

    std::cout << "x = " << x << std::endl;
    std::cout << "y = " << y << std::endl;
    std::cout << "pow(x, y) = " << pow(x, y) << std::endl;

    return 0;
}
