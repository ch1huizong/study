#include <iostream>
// T: 矩阵转置, 利用二维数组, 动态数组（多级指针)
// Value

void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    // 动态内存分配生成二维数组, HaHa
    int **a; // 二级指针, 有没有其他方式？有，指针数组
    a = new int *[3];
    for (int i = 0; i < 3; i++)
        a[i] = new int[3]; // a里的每个元素指向int数组首地址

    std::cout << "输入9个整数作为矩阵元素值: " << std::endl;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            std::cin >> a[i][j];

    std::cout << "初始矩阵: " << std::endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++)
            std::cout << a[i][j] << ' ';
        std::cout << std::endl;
    }

    for (int i = 0; i < 3; i++)
        for (int j = 0; j < i; j++)
            swap(a[i][j], a[j][i]);

    std::cout << "转置后矩阵: " << std::endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++)
            std::cout << a[i][j] << ' ';
        std::cout << std::endl;
    }

    return 0;
}
