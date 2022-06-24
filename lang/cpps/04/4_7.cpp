#include <iomanip>
#include <iostream>
#include <string>
// T: 结构体使用 - C++中的结构体是一种特殊的类

struct Student { // 与C结构体的定义相同了,当里面没有函数成员
    int num;
    std::string name;
    char sex;
    int age;
};

int main(int argc, char *argv[]) {
    Student stu = {97001, "Lin Lin", 'F', 19};

    std::cout << "Num: " << stu.num << std::endl;
    std::cout << "Name: " << stu.name << std::endl;
    std::cout << "Sex: " << stu.sex << std::endl;
    std::cout << "Age: " << stu.age << std::endl;

    return 0;
}
