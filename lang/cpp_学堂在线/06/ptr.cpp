#include <iostream>

int main(int argc, char *argv[]) {
    int i = 100;
    int *p = &i;

    std::cout << "i = " << i << std::endl;
    std::cout << "&i = " << &i << std::endl;
    std::cout << "p = " << p << std::endl;
    std::cout << "*p = " << *p << std::endl;
    std::cout << "&p = " << &p << std::endl;

    return 0;
}
