#include <iostream>
// T: 变量作用域 - 文件作用域/局部作用域

int i; // 文件作用域
int main(int argc, char *argv[]) {
    i = 5;
    {
        int i; // 局部作用域
        i = 7;
        std::cout << "i = " << i << std::endl;
    }
    std::cout << "i = " << i << std::endl;

    return 0;
}
