#include <iostream>
// T: 函数嵌套调用

int fun2(int m) { return m * m; }

int fun1(int x, int y) { return fun2(x) + fun2(y); }

int main(int argc, char *argv[]) {
    int a, b;
    std::cout << "Please enter two integers(a and b):";
    std::cin >> a >> b;
    std::cout << "The sum of square a and b is : " << fun1(a, b) << std::endl;

    return 0;
}
