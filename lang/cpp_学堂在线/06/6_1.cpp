#include <iostream>
// T: 数组的构建和访问

int main(int argc, char *argv[]) {
    int a[10], b[10];
    for (int i = 0; i < 10; ++i) {
        a[i] = i * 2 - 1;
        b[10 - i - 1] = a[i];
    }

    for (int i = 0; i < 10; ++i) {
        std::cout << "a[" << i << "] = " << a[i] << " ";
        std::cout << "b[" << i << "] = " << b[i] << std::endl;
    }

    return 0;
}
