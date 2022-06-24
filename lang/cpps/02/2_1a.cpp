#include <iostream>
// T: 变量

int main(int argc, char *argv[]) {
    int radius;

    std::cout << "Please enter the radius!\n";
    std::cin >> radius;
    std::cout << "The radius is:" << radius << '\n';
    std::cout << "PI is:" << 3.14 << '\n';

    std::cout << "Please enter a different radius!\n";
    std::cin >> radius;
    std::cout << "Now the radius is changed to:" << radius << '\n';

    return 0;
}
