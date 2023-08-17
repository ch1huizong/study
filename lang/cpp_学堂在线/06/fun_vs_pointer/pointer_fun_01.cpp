#include <iostream>
// T: 指针函数
// 寻找数组中第一个0元素地址

int main(int argc, char *argv[]) {
    int array[10];
    int *search(int *a, int num);

    for (int i = 0; i < 10; ++i) {
        std::cin >> array[i];
    }
    int *zeroptr = search(array, 10);

    if (zeroptr != nullptr) {
        std::cout << "Got: " << zeroptr << std::endl;
    } else {
        std::cout << "Failed! Not Found!" << std::endl;
    }

    return 0;
}

int *search(int *a, int num) {
    for (int i = 0; i < num; ++i) {
        if (a[i] == 0) {
            return &a[i];
        }
    }

    return nullptr;
}
