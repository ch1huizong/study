#include <iostream>
// T: 统计正负数

int main(int argc, char *argv[]) {
    int i = 0, j = 0, n;
    std::cout << "Enter some integers please (enter 0 to quit) :" << std::endl;

    std::cin >> n;
    while (n != 0) {
        if (n > 0) {
            i += 1;
        }
        if (n < 0) {
            j += 1;
        }
        std::cin >> n;
    }
    std::cout << "Count of positive integers:" << i << std::endl;
    std::cout << "Count of negative integers:" << j << std::endl;

    return 0;
}
