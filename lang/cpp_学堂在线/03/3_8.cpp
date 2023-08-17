#include <iostream>
// T: 递归函数-1

unsigned fac(int n) {
    unsigned f;

    if (n == 0) {
        f = 1;
    } else {
        f = n * fac(n - 1);
    }

    return f;
}

int main(int argc, char *argv[]) {
    unsigned n;

    std::cout << "Enter a positive integer:";
    std::cin >> n;
    unsigned y = fac(n);
    std::cout << n << "!=" << y << std::endl;

    return 0;
}
