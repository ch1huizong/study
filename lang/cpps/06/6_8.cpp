#include <iostream>
// T: 指针数组应用 - 另一种构造二维数组的方法

int main(int argc, char *argv[]) {
    int line1[] = {1, 0, 0};
    int line2[] = {0, 1, 0};
    int line3[] = {0, 0, 1};

    int *p[3] = {line1, line2, line3};
    // int (*q)[3]; // 这是什么？
    // std::cout << sizeof(p) << std::endl;

    std::cout << "Matrix test: " << std::endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            std::cout << p[i][j] << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
