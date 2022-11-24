#include <stdio.h>
// T: 静态本地变量,拥有全局生存期和本地作用域

int f(void);

int gAll = 12;

int main(int argc, char *argv[]) {
    f();
    f();
    f();

    return 0;
}

int f(void) {
    static int all = 1;  // 只初始化一次

    // int k = 0;
    // printf("&gAll = %p\n", &gAll);
    // printf("&all = %p\n", &all); // 和all处相同的内存区域
    // printf("&k = %p\n", &k);

    printf("in %s all = %d\n", __func__, all);
    all += 2;
    printf("again in %s all = %d\n", __func__, all);

    return all;
}
