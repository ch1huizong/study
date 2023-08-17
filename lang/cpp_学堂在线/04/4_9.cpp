#include <iostream>
// T: 枚举类 - 强制枚举类型

enum class Side {Right, Left};
enum class Thing {Wrong, Right}; // 与前一个Right不会冲突

enum class Sex:char { Man = 'M', Female = 'F' }; //指定底层类型

int main(int argc, char *argv[]) {
    Side s = Side::Right; // Side限定，强作用域
    Thing w = Thing::Wrong;

    std::cout << (s == w) << std::endl; // 编译错误，无法直接比较不同枚举类

    return 0;
}
