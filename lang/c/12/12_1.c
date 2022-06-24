#include <stdio.h>
// T: 全局变量

int f(void);

int gAll = 12; // 全局变量的初始化

int main(int argc, char *argv[]) {
    printf("in %s gAll = %d\n", __func__, gAll);
    f();
    printf("again in %s gAll = %d\n", __func__, gAll);

    return 0;
}

int f(void) {
    int gAll = 1; // 本地变量隐藏全局变量

    printf("in %s gAll = %d\n", __func__, gAll);
    gAll += 2;
    printf("again in %s gAll = %d\n", __func__, gAll);

    return gAll;
}
