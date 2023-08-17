#include <iostream>
// T: 函数指针

int max(int a, int b) { return ((a > b) ? a : b); }

int min(int a, int b) { return ((a < b) ? a : b); }

int sum(int a, int b) { return a + b; }

int compute(int a, int b, int (*f)(int a, int b)) { // 定义函数指针
    // return (*f)(a, b);
    return f(a, b);
}

int main(int argc, char *argv[]) {
    int a, b, res;
    std::cout << "请输入整数a: ";
    std::cin >> a;
    std::cout << "请输入整数b: ";
    std::cin >> b;

    res = compute(a, b, &max); // 可以直接传函数名max
    std::cout << "Max of " << a << " and " << b << " is " << res << std::endl;

    res = compute(a, b, &min);
    std::cout << "Min of " << a << " and " << b << " is " << res << std::endl;

    res = compute(a, b, &sum);
    std::cout << "Sum of " << a << " and " << b << " is " << res << std::endl;

    return 0;
}
