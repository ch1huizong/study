#include <iostream>
// T: 指针函数, 错误点

int main(int argc, char *argv[]) {
    int *function();
    int *ptr = function();
    *ptr = 5;

    return 0;
}

int *function() {
    int tmp = 0;
    return &tmp; // 会非法访问
}
