#include <iostream>
// T: 测试变量的作用域和生存期

int x = 1, y = 2;

void fn1();

int main(int argc, char *argv[]) {
    std::cout << "Begin..." << std::endl;
    std::cout << "x = " << x << std::endl;
    std::cout << "y = " << y << std::endl;

    std::cout << "Evaluate x and y in main.." << std::endl;
    int x = 10, y = 20;
    std::cout << "x = " << x << std::endl;
    std::cout << "y = " << y << std::endl;

    std::cout << "Step into fn1()..." << std::endl;
    fn1();

    std::cout << "Back in main" << std::endl;
    std::cout << "x = " << x << std::endl;
    std::cout << "y = " << y << std::endl;
    return 0;
}

void fn1() {
    int y = 200;
    std::cout << "x = " << x << std::endl;
    std::cout << "y = " << y << std::endl;
}
