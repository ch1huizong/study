#include <iostream>
// T: 变量的引用举例

int main(int argc, char *argv[]) {
    int i, j;
    int &ri = i; // 定义i的引用,两个都指向同一个对象

    j = 10;
    ri = j;

    std::cout << "j = " << j << std::endl;
    std::cout << "ri = " << ri << std::endl;
    std::cout << "i = " << i << std::endl;

    return 0;
}
