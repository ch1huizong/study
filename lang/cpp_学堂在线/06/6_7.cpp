#include <iostream>
// T: 数组的指针属性和指针的数组属性

int main(int argc, char *argv[]) {
    int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};

    std::cout << "Output by array index: ";
    for (int i = 0; i < 10; ++i) {
        std::cout << a[i] << " ";
    }
    std::cout << std::endl;

    std::cout << "Output by array name pointer: ";
    for (int i = 0; i < 10; ++i) {
        std::cout << *(a + i) << " ";
    }
    std::cout << std::endl;

    std::cout << "Output by pointer: ";
    for (int *p = a; p < a + 10; p++) {
        std::cout << *p << " ";
    }
    std::cout << std::endl;

    return 0;
}
