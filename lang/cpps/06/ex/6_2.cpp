#include <iostream>

#include "employee.h"

int main() {
    Employee e("Wang Er", "Haidian", "Beijing", "100084");
    e.display();
    e.change_name("Li San");
    e.display();

    return 0;
}
