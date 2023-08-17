#include <iostream>
// T: 无符号数

int main(int argc, char *argv[]) {
    // unsigned int x;
    int x;
    unsigned int y = 100;
    unsigned int z = 50;

    x = y - z;
    std::cout << "Difference is: " << x << std::endl;
    x = z - y;
    std::cout << "Now difference is: " << x << std::endl;

    return 0;
}
