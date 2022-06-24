#include <stdio.h>
// T: 前缀和后缀表达式的值

int main(int argc, char *argv[]) {
    int a = 10;

    printf("a++ = %d\n", a++); // 表达式的值
    printf("a = %d\n", a);

    printf("++a = %d\n", ++a);
    printf("a = %d\n", a);

    return 0;
}
