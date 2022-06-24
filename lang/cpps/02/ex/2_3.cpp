#include <iostream>
// T: cin使用

int main(int argc, char *argv[]) {
    int a, b, x;

    std::cout << "input value of a : ";
    std::cin >> a;

    std::cout << "input vblue of b : ";
    std::cin >> b;

    x = (a - b) > 0 ? (a - b) : (b - a);
    std::cout << "The difference of a and b is:\t\t" << x << std::endl;

    return 0;
}
