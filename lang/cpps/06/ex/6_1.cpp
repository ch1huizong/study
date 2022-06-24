#include <iostream>
// T: 矩阵转置, 利用二维数组, 静态数组

void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int a[3][3];
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

    for (int i = 0; i < 3; i++)     // 转置, 沿对角线翻转
        for (int j = 0; j < i; j++) // 注意条件,对角线下半部分
            swap(a[i][j], a[j][i]);

    std::cout << "转置后矩阵: " << std::endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++)
            std::cout << a[i][j] << ' ';
        std::cout << std::endl;
    }

    return 0;
}
