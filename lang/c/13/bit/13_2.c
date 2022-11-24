#include <stdio.h>
// T: 移位运算

int main(int argc, char *argv[]) {
    int a = 0x80000000;
    unsigned int b = 0x80000000;
    printf("a = %d\n", a);
    printf("b = %u\n", b);
    printf("\n");

    printf("右移:\n");
    printf("a>>1 = %d\n", a >> 1);  // 有符号位右移保持符号位不变
    printf("b>>1 = %u\n", b >> 1);
    printf("\n");

    printf("左移:\n");  // 空位填0
    printf("a<<1 = %d\n", a << 1);
    printf("b<<1 = %u\n", b << 1);

    return 0;
}
