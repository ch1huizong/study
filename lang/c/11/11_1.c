#include <stdio.h>
// T: 枚举 - 常量符号化

enum color {red, yellow, green};

void f(enum color c);

int main(int argc, char *argv[]) {
    enum color t = red; // 直接使用枚举量
    scanf("%d", &t);
    f(t);

    return 0;
}

void f(enum color c) { printf("%d\n", c); }
