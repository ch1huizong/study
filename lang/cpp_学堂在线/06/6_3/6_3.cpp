#include <iostream>

#include "Point.h"
// T: 对象数组使用

int main(int argc, char *argv[]) {
    std::cout << "Entering main..." << std::endl;
    Point a[2];
    for (int i = 0; i < 2; ++i) {
        a[i].move(i + 10, i + 20);
    }
    std::cout << "Exiting main..." << std::endl;

    return 0;
}
