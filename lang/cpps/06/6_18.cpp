#include <iostream>
// T: 创建多维度动态数组 - 此时注意左边的指针类型
// Value

int main(int argc, char *argv[]) {
    int(*cp)[9][8] = new int[7][9][8]; // cp的指向的内容块是数组

    for (int i = 0; i < 7; ++i) {
        for (int j = 0; j < 9; ++j) {
            for (int k = 0; k < 8; ++k) {
                *(*(*(cp + i) + j) + k) = (i * 100 + j * 10 + k); // 层层寻址
                // 其实，关键点是编译器知道cp +i, +j移动多少字节地址
            }
        }
    }

    for (int i = 0; i < 7; ++i) {
        for (int j = 0; j < 9; ++j) {
            for (int k = 0; k < 8; ++k) {
                std::cout << cp[i][j][k] << " ";
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
    }

    delete[] cp;

    return 0;
}
