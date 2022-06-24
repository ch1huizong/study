#include <cmath>
#include <iostream>
// T: 函数重载

int max1(int a, int b) {
    if (a == b) {
        return a;
    } else if (a > b) {
        return a;
    } else {
        return b;
    }
}

int max1(int a, int b, int c) { return max1(max1(a, b), c); }

double max1(double a, double b) {
    if (fabs(a - b) < 1e-10) {
        return a;
    } else if (a > b) {
        return a;
    } else {
        return b;
    }
}

double max1(double a, double b, double c) { return max1(max1(a, b), c); }

int main(int argc, char *argv[]) {
    int a, b, c;
    double m, n, l;

    std::cout << "Enter int a: ";
    std::cin >> a;
    std::cout << "Enter int b: ";
    std::cin >> b;
    std::cout << "Enter int c: ";
    std::cin >> c;

    std::cout << "max of " << a << " and " << b << " is " << max1(a, b)
              << std::endl;
    std::cout << "max of " << a << " and " << b << " and " << c << " is "
              << max1(a, b, c) << std::endl;

    std::cout << "Enter int m: ";
    std::cin >> m;
    std::cout << "Enter int n: ";
    std::cin >> n;
    std::cout << "Enter int l: ";
    std::cin >> l;
    std::cout << "max of " << m << " and " << n << " is " << max1(m, n)
              << std::endl;
    std::cout << "max of " << m << " and " << n << " and " << l << " is "
              << max1(m, n, l) << std::endl;

    return 0;
}
