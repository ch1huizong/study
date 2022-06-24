#include <iostream>

#include "Point.h"
// T: 类的使用实例

int main(int argc, char *argv[]) {
    Point a(4, 5);
    std::cout << "Point A: " << a.getX() << "," << a.getY() << std::endl;
    a.showCount();

    Point b(a);
    std::cout << "Point B: " << b.getX() << "," << b.getY() << std::endl;
    b.showCount();

    return 0;
}
