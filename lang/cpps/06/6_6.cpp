#include <iostream>
// T: void(无)类型指针使用

int main(int argc, char *argv[]) {
    // void abc; //不能声明void类型的变量
    void *pv; // 声明无类型指针
    int i = 5;
    pv = &i;

    int *pint = static_cast<int *>(pv); // void指针强制转换为int指针
    std::cout << "*pint = " << *pint << std::endl;

    return 0;
}
