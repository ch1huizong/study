#include <iostream>
// T: do-while
// 数字反转

int main(int argc, char *argv[]) {
    int n, right_digit, newnum = 0;

    std::cout << "Enter the number:";
    std::cin >> n;

    std::cout << "The number in reverse order is ";

    do {
        right_digit = n % 10; // 最右边数字
        std::cout << right_digit;
        n /= 10;

    } while (n != 0);
    std::cout << std::endl;

    return 0;
}
