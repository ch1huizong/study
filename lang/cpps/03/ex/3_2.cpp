#include <iostream>
// T: 递归版本的fib

int fib(int n);

int main(int argc, char *argv[]) {
    int n, answer; // 第n个fib数字是什么?

    std::cout << "Enter number: ";
    std::cin >> n;
    answer = fib(n);
    std::cout << answer << " is the " << n << "th fib number." << std::endl;

    return 0;
}

int fib(int n) {
    std::cout << "Processing fib(" << n << ")...";

    if (n == 1 || n == 2) {
        std::cout << "Return 1!" << std::endl;
        return 1;
    } else {
        std::cout << "Call fib(" << n - 1 << ")"
                  << " and fib(" << n - 2 << ")" << std::endl;
        return fib(n - 1) + fib(n - 2);
    }
}
