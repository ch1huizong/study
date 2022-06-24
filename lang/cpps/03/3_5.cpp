#include <cmath>
#include <iostream>
// T: 函数调用-5 - 计算分段函数

const double TINY_VALUE = 1e-10;

double tsin(double x) {
    double g = 0;
    double t = x;
    int n = 1;

    do {
        g += t;
        n++;
        t = -t * x * x / (2 * n - 1) / (2 * n - 2);
    } while (fabs(t) >= TINY_VALUE);

    return g;
}

int main(int argc, char *argv[]) {
    double k, r, s;
    std::cout << "r = ";
    std::cin >> r;
    std::cout << "s = ";
    std::cin >> s;

    if (r * r <= s * s) {
        k = sqrt(tsin(r) * tsin(r) + tsin(s) * tsin(s));
    } else {
        k = tsin(r * s) / 2;
    }
    std::cout << k << std::endl;

    return 0;
}
