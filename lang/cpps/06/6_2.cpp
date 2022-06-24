#include <iostream>
// T: 数组传给函数，计算数组各行之和并存储到数组各行首元素

void rowSum(int a[][4], int nRow) {
    for (int i = 0; i < nRow; ++i) {
        for (int j = 1; j < 4; ++j) {
            a[i][0] += a[i][j];
        }
    }
}

int main(int argc, char *argv[]) {
    int table[][4] = {{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}};
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 4; ++j) {
            std::cout << table[i][j] << " ";
        }
        std::cout << std::endl;
    }

    rowSum(table, 3);

    for (int i = 0; i < 3; ++i) {
        std::cout << "Sum of row " << i << " is " << table[i][0] << std::endl;
    }

    return 0;
}
