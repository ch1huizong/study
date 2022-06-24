#include <iostream>
// T: 流程控制-if

int main(int argc, char *argv[]) {
    int x, y;
    std::cout << "Enter x and y:";
    std::cin >> x >> y;

    if (x != y) {
        if (x > y) {
            std::cout << "x > y" << std::endl;

        } else {
            std::cout << "x < y" << std::endl;
        }

    } else {
        std::cout << "x = y" << std::endl;
    }

    return 0;
}
