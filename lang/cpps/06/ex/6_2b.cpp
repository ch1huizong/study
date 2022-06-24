#include <iostream>

#include "employee.h"
// T: 动态生成对象

int main() {
    Employee emp[5], *empOne = 0;

    empOne = new Employee("Zhang San", "Haidian", "Beijing", "100084");
    emp[0] = *empOne;
    delete empOne;

    empOne = new Employee("Li Si", "Xuanwu", "Beijing", "100031");
    emp[1] = *empOne;
    delete empOne;

    empOne = new Employee("Wang Wu", "Nanfu", "Shanghai", "012345");
    emp[2] = *empOne;
    delete empOne;

    empOne = new Employee("Zhu Ge", "Wuhou", "Chengdu", "543210");
    emp[3] = *empOne;
    delete empOne;

    empOne = new Employee("Sun ying", "Zhifu", "Yantai", "264000");
    emp[4] = *empOne;
    delete empOne;

    for (int i = 0; i < 5; i++) {
        std::cout << "Number" << i << ':' << std::endl;
        emp[i].display();
    }

    return 0;
}
