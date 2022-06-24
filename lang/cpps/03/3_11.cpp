#include <iostream>
// T: 值传递和引用传递

void swap(int a, int b) {
    int t = a;
    a = b;
    b = t;
}

void swap1(int &a, int &b) {
    int t = a;
    a = b;
    b = t;
}

int main(int argc, char *argv[]) {
    int x = 5, y = 10;

    std::cout << "值传递:" << std::endl;
    std::cout << "\tBefore: x = " << x << " y = " << y << std::endl;
    swap(x, y);
    std::cout << "\tAfter: x = " << x << " y = " << y << std::endl;

    std::cout << std::endl;

    std::cout << "引用传递:" << std::endl;
    std::cout << "\tBefore: x = " << x << " y = " << y << std::endl;
    swap1(x, y);
    std::cout << "\tAfter: x = " << x << " y = " << y << std::endl;

    return 0;
}
