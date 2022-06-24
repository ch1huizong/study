#include <iostream>
// T: 指针函数
// 子函数返回new的地址

int main(int argc, char *argv[]) {
    int *newintVar(void);

    int *intptr = newintVar();
    *intptr = 5;
    std::cout << "var: " << *intptr << std::endl;

    delete intptr;

    return 0;
}

int *newintVar(void) {
    int *p = new int;
    return p;
}
