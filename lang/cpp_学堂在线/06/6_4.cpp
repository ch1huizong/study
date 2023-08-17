#include <iostream>
// T: 数组(容器), 基于范围的for循环

int main(int argc, char *argv[]) {
    int a[3] = {1, 2, 3};
    int b[] = {4, 5, 6, 7, 8};

    int *p;
    for (p = a; p < a + sizeof(a) / sizeof(int); ++p) {
        *p += 2;
        std::cout << *p << std::endl;
    }

    std::cout << std::endl;

    for (int &e : b) { // e是数组中元素的别名?
        e += 2;
        std::cout << e << std::endl;
    }

    return 0;
}
