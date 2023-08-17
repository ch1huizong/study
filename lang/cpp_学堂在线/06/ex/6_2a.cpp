#include <iostream>

#include "employee.h"

int main() {
    Employee emp[5] = {Employee("Zhang San", "Haidian", "Beijing", "100084"),
                       Employee("Li Si", "Xuanwu", "Beijing", "100031"),
                       Employee("Wang Wu", "Nanfu", "Shanghai", "012345"),
                       Employee("Zhu Ge", "Wuhou", "Chengdu", "543210"),
                       Employee("Sun ying", "Zhifu", "Yantai", "264000")};

    for (int i = 0; i < 5; i++) {
        std::cout << "Number" << i << ':' << std::endl;
        emp[i].display();
        std::cout << std::endl;
    }

    return 0;
}
