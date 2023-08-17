#include <iostream>
// T: 测试基本数据类型长度

int main(int argc, char *argv[]) {
    std::cout << "The size of an int is:\t\t" << sizeof(int) << "bytes."
              << std::endl;
    std::cout << "The size of a short is:\t\t" << sizeof(short) << "bytes."
              << std::endl;
    std::cout << "The size of a long is:\t\t" << sizeof(long) << "bytes."
              << std::endl;
    std::cout << "The size of a char is:\t\t" << sizeof(char) << "bytes."
              << std::endl;
    std::cout << "The size of a float is:\t\t" << sizeof(float) << "bytes."
              << std::endl;
    std::cout << "The size of a double is:\t\t" << sizeof(double) << "bytes."
              << std::endl;

    return 0;
}
