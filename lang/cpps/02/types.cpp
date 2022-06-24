#include <iostream>
// T: 类型定义语法

typedef int int_32;
typedef unsigned int un_32;

using machine_32 = int;
using machine_64 = long;

int main() {
    int_32 a = 10;
    un_32 b = 65;

    printf("a = %d\n", a);
    printf("b = %d\n", b);

    printf("sizeof(machine_32) = %ld\n", sizeof(machine_32));
    printf("sizeof(machine_64) = %ld\n", sizeof(machine_64));

    auto v = a + b; // 类型取决于右边
    printf("v = %d\n", v);

    decltype(b) j = 2; // j是b类型
    printf("j = %d\n", j);

    return 0;
}
