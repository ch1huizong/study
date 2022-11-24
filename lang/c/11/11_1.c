// T: 枚举 - 常量符号化

#include <stdio.h>

enum color { red, yellow, green };

void f(enum color c);

int main(int argc, char *argv[]) {
    enum color t = red;  // 使用enum类型，枚举量进行赋值
    scanf("%d", &t);
    f(t);

    return 0;
}

void f(enum color c) { printf("%d\n", c); }
