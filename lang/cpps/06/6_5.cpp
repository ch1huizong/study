#include <iostream>
// T: 指针变量使用

int main(int argc, char *argv[]) {
    int i;
    int *ptr = &i;

    i = 10;
    std::cout << "i = " << i << std::endl;
    std::cout << "*ptr = " << *ptr << std::endl;

    return 0;
}
