#include <iostream>
// T: 流程控制-for

int main(int argc, char *argv[]) {
    int n;
    std::cout << "Enter a positive integer : ";
    std::cin >> n;
    std::cout << "Number " << n << " Factors ";

    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            std::cout << i << " ";
        }
    }
    std::cout << std::endl;

    return 0;
}
